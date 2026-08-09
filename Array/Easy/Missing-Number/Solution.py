class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumarr = sum(nums)
        actsum = (n*(n+1))/2
        return int(actsum - sumarr)
