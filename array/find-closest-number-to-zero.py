class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        pos = 999999
        neg = -pos
        for x in nums:
            if x < pos and neg < x:
                if x < 0:
                    neg = x
                else:
                    pos = x
        return pos if pos <= -neg else neg