class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        #BRUTEFORCE": if k < numOnes, we return k, else if it is less than numOnes+numZeroes, we still return numOnes, else we return Numones + (-1)*(k - (numZeroes+Numones), also if sum of all three is less than
        if k <= numOnes:
            return k
        elif k <= (numOnes+numZeros):
            return numOnes
        else:
            return numOnes + ((-1) * (k-(numZeros+numOnes)))
