class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        diff = 0
        idx = 0
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                idx = i
        if idx == 0:
            return True
        else:
            return ((nums[:idx] == sorted(nums[:idx])) and (nums[idx:] == sorted(nums[idx:])) 
            and  nums[-1] <= nums[0])

