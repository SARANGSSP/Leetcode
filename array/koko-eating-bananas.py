import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #if the length of the arr is equal to the num of hours, return the max element
        #if it is less than the num of hours, we subtract 1 from the max every time till we reach a value where the addition of ceiling of the division of all elements is less than the num of hours
        n = len(piles)
        if n == h:
            return max(piles)
        l = 1
        r = max(piles)
        ans = 0
        while l <= r:
            add = 0
            mid = (l+r)//2
            for i in range(n):
                add += math.ceil(piles[i]/mid)
            if add > h:
                l = mid + 1
            elif add <= h:
                r = mid - 1
                ans = mid
        return ans