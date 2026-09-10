class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg = 0,0
        n = len(nums)
        arr =[]
        while pos < n and neg < n:
            while nums[neg] > 0:
                neg += 1
            while nums[pos] < 0:
                pos += 1
            arr.append(nums[pos])
            arr.append(nums[neg])
            pos += 1
            neg += 1
        return arr