class Solution:
    # we go from 0 to n- 1
    # we compare mid to mid + 1 and mid -1, if it is peak return that else
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1
        r = n - 2
        if n == 1:
            return 0

        if nums[n-1] > nums[n-2]:
            return n-1

        if nums[0] > nums[1]:
            return 0
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid+1] > nums[mid]:
                l = mid + 1
            else:
                r = mid -1