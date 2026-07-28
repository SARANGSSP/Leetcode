class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        val = 0
        for i in range(n):
            val ^= nums[i]
        return val
                
        