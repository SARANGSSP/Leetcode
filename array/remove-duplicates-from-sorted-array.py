class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            if nums[i] > nums[counter]:
                nums[counter +1] = nums[i]
                counter += 1
        return counter +1 

