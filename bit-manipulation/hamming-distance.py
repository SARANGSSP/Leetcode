#convert both to binary number
#check which of them is longer a

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_int = str(bin(x)[2::])
        bin2_int = str(bin(y)[2::])

        a = len(bin_int)
        b = len(bin2_int)
        
        ham_dist = 0
        if a > b:
            bin2_int = "0"*(a-b) + bin2_int
        else:
            bin_int = "0"*(b-a) + bin_int

        for i in range(len(bin_int)):
            if bin_int[i] != bin2_int[i]:
                ham_dist += 1
        return ham_dist
