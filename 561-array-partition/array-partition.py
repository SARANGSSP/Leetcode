class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        a = sorted(nums)[::2]
        maxsum = 0
        return sum(a)
        


