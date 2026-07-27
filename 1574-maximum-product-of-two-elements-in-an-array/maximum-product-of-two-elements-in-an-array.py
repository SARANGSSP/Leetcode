#there are two ways of solving this: 1. is to sort and return max 2. is to find the two largest abs values and return their multiplication but only do that if both values are negative
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = sorted(nums)
        return max((a[0]-1)*(a[1]-1),(a[-1] -1)*(a[-2] -1))
        