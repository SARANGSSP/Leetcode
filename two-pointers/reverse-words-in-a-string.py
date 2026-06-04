class Solution:
    def reverseWords(self, s: str) -> str:
        out = s.strip().split()
        out = out[::-1]
        return(" ".join(out))