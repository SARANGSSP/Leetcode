class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0

        for num in num_set:
            if num - 1 not in num_set:        # only start counting at sequence start
                length = 1
                while num + length in num_set:
                    length += 1
                max_count = max(max_count, length)

        return max_count