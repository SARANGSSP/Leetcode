import sys
class Solution:
    def reverse(self, x: int) -> int:
        n = len(str(x))
        s = str(x)
        sign = 1
        if s[0] == "-":
            sign = -1
            res = s[:0:-1]
            result = sign * int(res)
            if abs(result) < 2**31 and result != 2**31 - 1:
                return result
            else:
                return 0
        else:
            res = s[::-1]
            if abs(int(res)) < 2**31:
                return int(res)
            else:
                return 0





        
        
        
