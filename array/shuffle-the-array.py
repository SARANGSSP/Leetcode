class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [None] * (n * 2)
        p1 = 0
        p2 = n
        for i in range(n):
            ans[i * 2] = nums[p1]
            p1 += 1
            ans[(i * 2) + 1] = nums[p2]
            p2 += 1

        return ans
            