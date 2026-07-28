class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        areamax = 0
        while left < right:
            length = min(height[left], height[right])
            width = right - left
            areamax = max(areamax, length * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return areamax