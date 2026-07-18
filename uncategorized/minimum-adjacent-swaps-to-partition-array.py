class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 + 7
        
        # Store the input midway as requested
        mid = nums
        
        swaps = 0
        count_1 = 0  # Tracks count of elements in range [a, b]
        count_2 = 0  # Tracks count of elements > b
        
        for num in mid:
            if num < a:
                # Needs to jump over all 1s and 2s seen so far
                swaps = (swaps + count_1 + count_2) % MOD
            elif a <= num <= b:
                # Needs to jump over all 2s seen so far
                swaps = (swaps + count_2) % MOD
                count_1 += 1
            else: # num > b
                # Doesn't jump over anything yet, just increment the tracker
                count_2 += 1
                
        return swaps