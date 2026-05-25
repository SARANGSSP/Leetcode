class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = 0
        ones = 0
        twos = 0
        n = len(nums)
        for i in range(0,n):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1
            else:
                twos += 1
        nums[:] = [0] * zeros + [1] * ones + [2] * twos
        """
        Do not return anything, modify nums in-place instead.
        """


        