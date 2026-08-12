class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = max(nums)
        hashmap = Counter(nums)
        for i in range(1,n):
            if i not in hashmap:
                return i
        if n > 0:
            return n+1
        else:
            return 1