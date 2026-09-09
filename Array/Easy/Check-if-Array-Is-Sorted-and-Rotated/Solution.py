class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        diff = 0
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                diff += 1

        return diff <= 1

