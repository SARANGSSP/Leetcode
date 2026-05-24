class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maximum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            elif nums[i] == 0:
                maximum = max(counter, maximum)
                counter = 0
        return max(counter, maximum)
