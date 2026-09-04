class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        for i in range(n):
            maxarr = max(nums[:i+1])
            minarr = min(nums[i:])
            if maxarr-minarr <= k:
                return i
        return -1