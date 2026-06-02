class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = {0:1}
        currSum = 0

        for n in nums:
            currSum += n
            diff = currSum - k

            res += prefix_sum.get(diff,0)
            prefix_sum[currSum] = 1 + prefix_sum.get(currSum, 0)
        return res