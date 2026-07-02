class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a = str(x)
        sum = 0
        for i in range(len(a)):
            sum = sum + int(a[i])
        if x % sum == 0:
            return sum
        else:
            return -1