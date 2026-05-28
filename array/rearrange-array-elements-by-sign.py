class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]* n
        pos_idx = 0
        neg_idx = 1
        
        for i in range(n):
            if nums[i] < 0:
                arr[neg_idx] = nums[i]
                neg_idx += 2
            else:
                arr[pos_idx] = nums[i]
                pos_idx += 2
        return arr

        