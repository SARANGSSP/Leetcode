#!/usr/bin/env python3
"""
backdate_leetcode_commits.py

Fetches your real accepted-submission timestamps from LeetCode and creates
one git commit per problem, backdated to when you actually solved it --
instead of one bulk commit dated today.

Run this AFTER organize_leetcode_by_topic.py, from inside your target git
repo (the one you'll push to GitHub).

Usage:
    pip install requests
    cd path/to/your/Leetcode/repo
    cp -r path/to/organized/* .
    python backdate_leetcode_commits.py --cookies "<full cookie string>" --files-dir .

This will:
  1. Query LeetCode for every accepted submission's timestamp + problem slug
  2. Match each timestamp to the corresponding file already copied into the repo
  3. `git add` + commit each file individually with GIT_AUTHOR_DATE /
     GIT_COMMITTER_DATE set to the real solve time, oldest first
  4. Leave the push to you (review `git log` before pushing)
"""

import argparse
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

SUBMISSION_QUERY = """
query submissionList($offset: Int!, $limit: Int!, $lastKey: String) {
  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey) {
    lastKey
    hasNext
    submissions {
      id
      statusDisplay
      lang
      timestamp
      titleSlug
    }
  }
}
"""


def fetch_all_accepted_submissions(cookies: str) -> dict:
    """Returns {title_slug: earliest_accepted_unix_timestamp}"""
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookies,
        "Referer": "https://leetcode.com/submissions/",
        "User-Agent": "Mozilla/5.0",
        "x-csrftoken": next(
            (c.split("=", 1)[1] for c in cookies.split(";") if c.strip().startswith("csrftoken=")),
            "",
        ),
    }

    earliest: dict = {}
    offset = 0
    limit = 20
    last_key = None

    while True:
        resp = requests.post(
            GRAPHQL_URL,
            json={
                "query": SUBMISSION_QUERY,
                "variables": {"offset": offset, "limit": limit, "lastKey": last_key},
            },
            headers=headers,
            timeout=10,
        )
        resp.raise_for_status()
        payload = resp.json().get("data", {}).get("submissionList")
        if not payload:
            print("  [warn] unexpected response, stopping pagination. Check your cookies.")
            break

        for sub in payload.get("submissions", []):
            if sub.get("statusDisplay") != "Accepted":
                continue
            slug = sub["titleSlug"]
            ts = int(sub["timestamp"])
            if slug not in earliest or ts < earliest[slug]:
                earliest[slug] = ts

        print(f"  fetched {offset + limit} submissions so far...")

        if not payload.get("hasNext"):
            break
        last_key = payload.get("lastKey")
        offset += limit
        time.sleep(0.5)  # be polite to LeetCode's API

    return earliest


def find_file_for_slug(files_dir: Path, slug: str) -> Path | None:
    for path in files_dir.rglob(f"{slug}.*"):
        if path.is_file():
            return path
    return None


def git_commit_with_date(repo_dir: Path, filepath: Path, unix_ts: int, message: str) -> bool:
    """Returns True if a commit was made, False if there was nothing new to commit."""
    dt = datetime.fromtimestamp(unix_ts, tz=timezone.utc)
    date_str = dt.strftime("%Y-%m-%dT%H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    rel_path = filepath.relative_to(repo_dir)
    subprocess.run(["git", "add", str(rel_path)], cwd=repo_dir, check=True)

    # Check if this file actually has staged changes before committing.
    # Already-existing/unchanged files would otherwise cause `git commit`
    # to fail with "nothing to commit" and crash the run.
    diff_check = subprocess.run(
        ["git", "diff", "--cached", "--quiet", "--", str(rel_path)],
        cwd=repo_dir,
    )
    if diff_check.returncode == 0:
        # no staged changes -- file already matches what's committed
        return False

    subprocess.run(
        ["git", "commit", "-m", message, "--date", date_str],
        cwd=repo_dir,
        env=env,
        check=True,
    )
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cookies", required=True, help="Full LeetCode cookie header string")
    parser.add_argument("--files-dir", default=".", help="Repo root containing the organized files")
    parser.add_argument("--dry-run", action="store_true", help="Print planned commits without running git")
    args = parser.parse_args()

    repo_dir = Path(args.files_dir).resolve()

    print("Fetching your accepted submission history from LeetCode...")
    earliest = fetch_all_accepted_submissions(args.cookies)
    print(f"Found {len(earliest)} unique solved problems.\n")

    # sort chronologically so commit history reads in real order
    ordered = sorted(earliest.items(), key=lambda kv: kv[1])

    committed, skipped, missing = 0, 0, []

    for slug, ts in ordered:
        filepath = find_file_for_slug(repo_dir, slug)
        if not filepath:
            missing.append(slug)
            continue

        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        message = f"Solve {slug} ({dt.strftime('%Y-%m-%d')})"

        if args.dry_run:
            print(f"  [dry-run] would commit {filepath.relative_to(repo_dir)} dated {dt}")
            committed += 1
        else:
            made_commit = git_commit_with_date(repo_dir, filepath, ts, message)
            if made_commit:
                print(f"  committed {filepath.relative_to(repo_dir)} dated {dt.date()}")
                committed += 1
            else:
                print(f"  [skip] {filepath.relative_to(repo_dir)} already up to date, no commit needed")
                skipped += 1

    print(f"\nDone. {committed} commits {'planned' if args.dry_run else 'created'}, {skipped} already up to date.")
    if missing:
        print(f"\n{len(missing)} solved problems had no matching file (not yet exported/organized):")
        for slug in missing[:20]:
            print(f"  - {slug}")
        if len(missing) > 20:
            print(f"  ...and {len(missing) - 20} more")

    if not args.dry_run:
        print("\nReview with `git log --oneline` before pushing. Then: git push")


if __name__ == "__main__":
    main()
