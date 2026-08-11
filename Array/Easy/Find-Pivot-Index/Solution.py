class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            a = nums[:i]
            b = nums[i+1:]
            if sum(a) == sum(b):
                return i
        return -1

