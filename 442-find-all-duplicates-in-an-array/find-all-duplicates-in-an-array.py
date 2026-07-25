class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashmap = {}
        res = []
        for i in range(n):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            if hashmap[nums[i]] == 2:
                res.append(nums[i])
        return res


