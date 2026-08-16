class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n):
            if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                return i
            