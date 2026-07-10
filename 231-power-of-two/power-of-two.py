class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a = str(bin(n))[2::].replace("0", "")
        print(a)
        if a == "1":
            return True
        else:
            return False