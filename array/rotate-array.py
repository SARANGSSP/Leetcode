class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last = len(nums) - 1

        while k>0:
            nums.insert(0,nums[last])
            nums.pop()
            k -= 1
        
        return nums

        