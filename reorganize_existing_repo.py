#!/usr/bin/env python3
"""
reorganize_existing_repo.py

Your repo already has LeetSync-created folders like:
    20-valid-parentheses/
    26-remove-duplicates-from-sorted-array/
sitting alongside the new topic folders (array/, hash-table/, etc.)
from organize_leetcode_by_topic.py.

This script finds those leftover LeetSync-style folders, looks up each
problem's topic tag, and moves its contents into the matching topic
folder using `git mv` (keeps it a tracked rename, not delete+recreate).
It leaves LeetSync's own README.md / Notes.md files alongside the code.

Run from inside the repo root.

Usage:
    pip install requests
    cd path/to/your/Leetcode/repo
    python reorganize_existing_repo.py --dry-run
    python reorganize_existing_repo.py
    git commit -m "Reorganize existing solutions into topic folders"
    git push
"""

import argparse
import json
import re
import subprocess
import time
from pathlib import Path

import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query questionTags($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    topicTags {
      name
      slug
    }
  }
}
"""

# Folders that are already topic destinations or infra -- never treat these as
# LeetSync problem folders to be moved.
SKIP_DIRS = {
    ".git", "organized", "__pycache__", ".github",
}


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def guess_title_slug(folder_name: str) -> str:
    """LeetSync folders look like '20-valid-parentheses' -> 'valid-parentheses'."""
    name = folder_name
    m = re.match(r"^\d+[-_]?(.*)$", name)
    if m and m.group(1):
        name = m.group(1)
    return slugify(name)


def fetch_tags(title_slug: str, cache: dict) -> dict | None:
    if title_slug in cache:
        return cache[title_slug]
    try:
        resp = requests.post(
            GRAPHQL_URL,
            json={"query": QUERY, "variables": {"titleSlug": title_slug}},
            headers={
                "Content-Type": "application/json",
                "Referer": f"https://leetcode.com/problems/{title_slug}/",
                "User-Agent": "Mozilla/5.0",
            },
            timeout=10,
        )
        resp.raise_for_status()
        question = resp.json().get("data", {}).get("question")
        cache[title_slug] = question
        time.sleep(0.4)
        return question
    except Exception as e:
        print(f"  [warn] failed to fetch tags for {title_slug}: {e}")
        cache[title_slug] = None
        return None


def is_known_topic_dir(path: Path, topic_names: set) -> bool:
    return path.name in topic_names


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print planned moves without running git mv")
    args = parser.parse_args()

    repo_root = Path(".").resolve()
    cache_path = repo_root / "_tag_cache.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}

    # Any folder already created by the topic-organizer counts as a "known topic"
    # once we've seen at least one problem routed there -- but simplest is to just
    # treat any directory whose name doesn't look like a LeetSync '<num>-slug' folder
    # as a topic folder (or something else) and leave it alone.
    leetsync_pattern = re.compile(r"^\d+-[a-z0-9-]+$")

    candidate_folders = [
        p for p in repo_root.iterdir()
        if p.is_dir() and p.name not in SKIP_DIRS and leetsync_pattern.match(p.name)
    ]

    print(f"Found {len(candidate_folders)} existing LeetSync-style folders to reorganize.\n")

    moved, skipped, conflicts = 0, [], []

    for folder in candidate_folders:
        title_slug = guess_title_slug(folder.name)
        question = fetch_tags(title_slug, cache)

        if not question or not question.get("topicTags"):
            topic = "uncategorized"
        else:
            topic = slugify(question["topicTags"][0]["name"])

        topic_dir = repo_root / topic
        topic_dir.mkdir(exist_ok=True)

        # Move every file inside the LeetSync folder (code, README, Notes.md, etc.)
        # into topic_dir, prefixed with the slug so filenames stay unique/traceable.
        files = [f for f in folder.iterdir() if f.is_file()]
        if not files:
            skipped.append(folder.name)
            continue

        for f in files:
            if f.suffix.lower() == ".md":
                target_name = f"{title_slug}-{f.stem}{f.suffix}"
            else:
                target_name = f"{title_slug}{f.suffix}"
            target_path = topic_dir / target_name

            rel_src = f.relative_to(repo_root)
            rel_dst = target_path.relative_to(repo_root)

            if target_path.exists():
                # Already covered by the backdate step (duplicate solve/export).
                # Don't overwrite -- flag it for manual review instead of crashing.
                conflicts.append((str(rel_src), str(rel_dst)))
                print(f"  [conflict] {rel_dst} already exists -- skipping {rel_src}")
                continue

            if args.dry_run:
                print(f"  [dry-run] git mv {rel_src} -> {rel_dst}")
            else:
                try:
                    subprocess.run(["git", "mv", str(rel_src), str(rel_dst)], check=True)
                    print(f"  moved {rel_src} -> {rel_dst}")
                except subprocess.CalledProcessError:
                    # git mv can fail if the file was already moved on disk in a
                    # previous partial run but not yet committed -- try a plain
                    # filesystem move + git add instead so the run can continue.
                    try:
                        f.rename(target_path)
                        subprocess.run(["git", "add", str(rel_dst)], check=True)
                        subprocess.run(["git", "add", "-u", str(rel_src)], check=False)
                        print(f"  moved (fallback) {rel_src} -> {rel_dst}")
                    except Exception as e:
                        conflicts.append((str(rel_src), f"ERROR: {e}"))
                        print(f"  [error] could not move {rel_src}: {e}")
                        continue

        moved += 1

        # Remove the now-empty LeetSync folder (git mv already emptied it of tracked
        # files; this cleans up the leftover directory on disk).
        if not args.dry_run:
            try:
                folder.rmdir()
            except OSError:
                pass  # non-empty (untracked leftovers) -- leave it for manual check

    cache_path.write_text(json.dumps(cache, indent=2), encoding="utf-8")

    print(f"\nDone. {moved} problem folders {'planned to move' if args.dry_run else 'moved'}.")
    if skipped:
        print(f"{len(skipped)} folders had no files and were skipped: {skipped}")
    if conflicts:
        print(f"\n{len(conflicts)} files had a naming collision with an already-existing file")
        print("(likely a duplicate from the backdate step) and were left in place for you to review:")
        for src, dst in conflicts:
            print(f"  {src}  ->  {dst}")

    if not args.dry_run and moved:
        print("\nNext: git commit -m \"Reorganize existing solutions into topic folders\" && git push")


if __name__ == "__main__":
    main()
