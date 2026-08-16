class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        c0 = 0
        c1 = 0
        c2 = 0
        for i in range(n):
            if nums[i] == 0:
                c0 += 1
            elif nums[i] == 1:
                c1 += 1
            else:
                c2+= 1
        i = 0
        while i < n:
            if c0 > 0:
                nums[i] = 0
                c0 -= 1
            elif c1 > 0:
                nums[i] = 1
                c1 -= 1
            else:
                nums[i] = 2
                c2 -= 1
            i += 1
        return nums
