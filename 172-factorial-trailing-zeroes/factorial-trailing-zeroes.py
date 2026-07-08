import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        a = math.factorial(n)
        count = 0
        flag = True
        while(flag):
            if a % 10 == 0:
                count += 1
                a = a//10
            else:
                flag = False 
        return count



        