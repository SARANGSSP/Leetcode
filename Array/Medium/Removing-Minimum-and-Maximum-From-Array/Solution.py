class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        mini = min(nums)
        maxi = max(nums)
        for i in range(n):
            if nums[i] == mini:
                x = i
            if nums[i] == maxi:
                y = i
        
        res = float('inf')
        if x < y: 
            res = min(res, y+1)
            res = min(res, n-x)
            res = min(res, (1+x + (n-y)))
        elif x > y:
            res = min(res, x+1)
            res = min(res, n-y)
            res = min(res, (1+y + (n-x)))
        return res