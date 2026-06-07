class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxi = 0
        res = ""
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]          # j+1 so the character at j is included
                if sub == sub[::-1] and len(sub) > maxi:
                    res = sub
                    maxi = len(sub)
        return res