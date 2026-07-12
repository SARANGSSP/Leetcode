class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        maxi = 0
        sum = 0
        for element in nums:
            largest_digit = int(max(str(element)))
            smallest_digit = int(min(str(element)))
            range = largest_digit - smallest_digit
            if range > maxi:
                maxi = range
                sum = 0
                sum += element
            elif range == maxi:
                sum += element
        return sum