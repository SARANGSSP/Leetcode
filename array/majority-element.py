class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moores Voting algorithm
        count = 0
        n = len(nums)
        el = nums[0]
        for i in range(0,n):
            if nums[i] == el:
                count += 1
            else:
                count -= 1
            if count == 0:
                el = nums[i]
                count += 1
        return el




        