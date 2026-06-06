class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        start = -1
        stop = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                start = mid
                stop = mid
                while start > 0 and nums[start] == nums[start-1]:
                    start -= 1
                while stop < len(nums) - 1 and nums[stop] == nums[stop+1]:
                    stop += 1
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return[start,stop]

       

        