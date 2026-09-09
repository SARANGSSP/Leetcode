class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        q = k%n
        arr = nums[n-q:] + nums[:n-q]
        print(arr)
        for i in range(n):
            nums[i] = arr[i]

        