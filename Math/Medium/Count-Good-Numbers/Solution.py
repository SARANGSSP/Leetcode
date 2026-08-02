class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_count = (n + 1) // 2   # indices 0, 2, 4, ... → 5 choices
        odd_count = n // 2          # indices 1, 3, 5, ... → 4 choices
        return (pow(5, even_count, MOD) * pow(4, odd_count, MOD)) % MOD