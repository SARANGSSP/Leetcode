class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            if target - nums[i] in hashmap:
                return [i,hashmap[target-nums[i]]]
            else:
                hashmap[nums[i]] = i