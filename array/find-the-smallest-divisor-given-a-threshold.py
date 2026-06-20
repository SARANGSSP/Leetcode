#we go from 1 to max(nums)
#divide whole array by mid check if equal to threshold, return the num at mid
#else: if num is higher than threshold: we move the low to mid and otherwise move high to mid
#if the number is less than threshold we store it in ans but there could be a smaller num so we move high to mid no ?

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        l = 1
        r = max(nums)
        ans = 0
        while l <= r:
            add = 0
            mid = (l+r)//2
            for i in range(n):
                add += math.ceil(nums[i]/mid)
            if add <= threshold:
                r = mid -1
                ans = mid
            else:
                l = mid +1
        return (ans) 