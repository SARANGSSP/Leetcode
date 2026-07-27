class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            l,r = 0,0
            num = 0
            odds = 0
            while r < len(nums):
                if nums[r] % 2 != 0:
                    odds += 1
                while odds > k:
                    if nums[l] %2 == 1:
                        odds -= 1
                    l+= 1
                num += (r-l + 1)
                r+= 1
            return num
        return atMost(k) - atMost(k-1)