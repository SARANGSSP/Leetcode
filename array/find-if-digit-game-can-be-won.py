class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        n = len(nums)
        single_dig = 0
        double_dig = 0
        for i in range(n):
            if nums[i] - 10 < 0:
                single_dig += nums[i]
            else:
                double_dig += nums[i]
        if single_dig == double_dig:
            return False
        else:
            return True