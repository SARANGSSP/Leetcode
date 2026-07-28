class Solution:
    def minimumFlips(self, n: int) -> int:
        num = bin(n)
        b = str(num)[2::]
        a= b[::-1]
        counter = 0
        for i in range(len(b)):
            if a[i] != b[i]:
                counter += 1
        return counter
