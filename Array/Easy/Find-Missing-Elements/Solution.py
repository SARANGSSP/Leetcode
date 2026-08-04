class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = max(nums)
        b = min(nums)
        result = []
        for i in range(b,a+1):
            if i not in nums:
                result.append(i)
        return result