class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans = 0
        if n <= 8:
            ans += n
        elif n > 8 and n <= 16:
            ans = 8 + ((n-8)*2)
        elif n > 16 and n <= 24:
            ans = 24 + ((n - 16)*3)
        else:
            ans = 48 + ((n-24)*4)
        return ans
