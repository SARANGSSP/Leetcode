class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        summation = 0
        maximum = float("-inf")
        if n == 1:
            return nums[0]
        for i in range(n):
            summation += nums[i]
            maximum = max(maximum,summation)
            if summation < 0:
                summation = 0
        return maximum

            
