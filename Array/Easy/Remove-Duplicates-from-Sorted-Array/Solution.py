class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != nums[j]:
                j+= 1
                nums[j] = nums[i]
        return j+1
