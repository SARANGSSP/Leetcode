class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def best_diff(i, j):
            if i > j:
                return 0
            take_left = nums[i] - best_diff(i + 1, j)
            take_right = nums[j] - best_diff(i, j - 1)
            return max(take_left, take_right)

        return best_diff(0, len(nums) - 1) >= 0