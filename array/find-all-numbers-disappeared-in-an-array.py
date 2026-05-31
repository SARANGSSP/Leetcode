class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n
        missing = []
        for i in range(n):
            arr[nums[i]-1] += 1
        for i in range(n):
            if arr[i] == 0:
                missing.append(i+1)
        return missing