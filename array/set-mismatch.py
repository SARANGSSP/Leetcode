class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * len(nums)
        for i in range(n):
            arr[nums[i]-1] += 1
        return([arr.index(2) +1 ,arr.index(0)+1])
