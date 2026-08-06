class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range (n,101):
            product = 1
            num = i
            while num > 0:
                product *= num % 10
                num //= 10
            if product == 0:
                return i
            elif product % t == 0:
                return i
