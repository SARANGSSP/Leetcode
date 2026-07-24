class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r,maxlen = 0,0,0
        numzero = 0
        for i in range(len(nums)):
            r = i
            if nums[i] == 0:
                numzero += 1
            if numzero > k:
                if nums[l] == 0:
                    l += 1
                    numzero -= 1
                else:
                    l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen
