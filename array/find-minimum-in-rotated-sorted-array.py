from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mini = float("inf")
        
        while low <= high:
            mid = (low + high) // 2
            
            # Case 1: The left half is sorted
            if nums[low] <= nums[mid]:
                mini = min(mini, nums[low])  # The smallest in a sorted left half is at 'low'
                low = mid + 1                # Eliminate left half, search right
                
            # Case 2: The right half is sorted
            else:
                mini = min(mini, nums[mid])  # The smallest in a sorted right half is at 'mid'
                high = mid - 1               # Eliminate right half, search left
                
        return mini