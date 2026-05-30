class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative = 0
        i = 0
        zero = 0
        while(i < len(nums) and nums[i] <= 0):
            if nums[i] < 0:
                negative += 1
                i += 1
            else:
                zero += 1
                i += 1

        return(max(negative, (len(nums)-negative-zero)))