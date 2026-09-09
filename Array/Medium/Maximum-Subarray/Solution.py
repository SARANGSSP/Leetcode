class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        n = len(nums)
        sumarr = 0
        maxarr = min(nums)
        for i in range(n):
            sumarr += nums[i]
            if sumarr < 0:
                sumarr = 0
            maxarr = max(maxarr,sumarr)
        return maxarr
