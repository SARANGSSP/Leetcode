class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l1 = l2 = 0
        sum1 = sum2 = 0
        res = 0
        for r in range(len(nums)):
            sum1 += nums[r]
            sum2 += nums[r]
            
            while l1 <= r and sum1 > goal:
                sum1 -= nums[l1]
                l1 += 1
            while l2 <= r and sum2 > goal - 1:
                sum2 -= nums[l2]
                l2 += 1
            res += (r - l1 + 1) - (r - l2 + 1)
        return res


