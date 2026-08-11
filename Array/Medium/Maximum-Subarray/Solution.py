class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        sumi = 0
        maxsum = float(-inf)
        for i in range(n):
            sumi += nums[i]
            maxsum = max(maxsum,sumi)
            if sumi < 0:
                sumi = 0
        return maxsum

