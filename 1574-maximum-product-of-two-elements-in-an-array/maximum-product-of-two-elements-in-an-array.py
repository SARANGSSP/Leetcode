#there are two ways of solving this: 1. is to sort and return max 2. is to find the two largest abs values and return their multiplication but only do that if both values are negative
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg_max, neg_sec, pos_max,pos_sec = 0,0,0,0
        flag = False
        for i in range(len(nums)):
            if nums[i] < 0 and nums[i] <= neg_max:
                neg_sec = neg_max
                neg_max = nums[i]
                flag = True
            elif nums[i] > 0 and nums[i] >= pos_max:
                pos_sec = pos_max
                pos_max = nums[i]
            else:
                if nums[i] >= pos_sec:
                    pos_sec = nums[i]
        pos_prod = (pos_max - 1) * (pos_sec - 1)
        neg_prod = (neg_max - 1) * (neg_sec -1)
        if flag:
            return max(pos_prod,neg_prod)
        else:
            return pos_prod