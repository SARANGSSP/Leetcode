class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return True
           
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
    
            elif nums[mid] >= nums[low]:

                if target < nums[mid] and target >= nums[low]:
                    high = mid -1
                else:
                    low = mid +1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid +1
                else:
                    high = mid - 1
        return False
