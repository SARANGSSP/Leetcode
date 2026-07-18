class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
        mid = n // 2
        max_val = s + (mid * m) - (mid - 1)
        return max_val