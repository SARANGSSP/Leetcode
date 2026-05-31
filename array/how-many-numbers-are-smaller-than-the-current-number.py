class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        for i in nums:
            freq[i] += 1

        for i in range(1, len(freq)):
            freq[i] += freq[i-1]

        res = []
        
        for i in nums:
            res.append(freq[i-1] if i - 1 >= 0 else 0)

        return res