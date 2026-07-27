#there are two ways of solving this: 1. is to sort and return max 2. is to find the two largest abs values and return their multiplication but only do that if both values are negative
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos_max,pos_sec = 0,0
        for i in range(len(nums)):
            if nums[i] >= pos_max:
                pos_sec = pos_max
                pos_max = nums[i]
            else:
                if nums[i] >= pos_sec:
                    pos_sec = nums[i]
        pos_prod = (pos_max - 1) * (pos_sec - 1)
        return pos_prod