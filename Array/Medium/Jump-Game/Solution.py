class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxind = 0
        for i in range(n):
            if i > maxind:
                return False
            maxind = max(maxind, i + nums[i])
        return True