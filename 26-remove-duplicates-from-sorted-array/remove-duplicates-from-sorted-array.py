class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == nums[j]:
                i += 1
            else:
                j += 1
                nums[j] = nums[i]
        return j+1

