class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = sorted(nums)
        return max(a[0]*a[1]*a[-1], a[-1]*a[-2]*a[-3])