import math

class Solution:
    def climbStairs(self, n: int) -> int:
        total_ways = 0
        # i is the number of 2-steps we can take.
        # We can take anywhere from 0 up to n // 2 of them.
        for i in range(n // 2 + 1):
            total_ways += math.comb(n - i, i)
        return total_ways