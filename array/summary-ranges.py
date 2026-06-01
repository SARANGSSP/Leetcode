class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        n = len(nums)
        i = 0
        j = 1
        arr = []

        while j <= n - 1:
            if nums[j] - 1 != nums[j - 1]:
                arr.append(nums[i])
                arr.append(nums[j - 1])
                i = j
            j += 1

        # Append the last range
        arr.append(nums[i])
        arr.append(nums[n - 1])

        # Build output
        out = []
        k = 0
        while k < len(arr):
            if arr[k] == arr[k + 1]:
                out.append(str(arr[k]))
            else:
                out.append(f"{arr[k]}->{arr[k+1]}")
            k += 2

        return out