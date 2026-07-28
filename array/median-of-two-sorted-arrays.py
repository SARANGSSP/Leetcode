class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        i = j = 0
        prev = curr = -1

        # walk the merged sequence up to the middle
        for _ in range(total // 2 + 1):
            prev = curr
            if i < n1 and (j >= n2 or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if total % 2 == 0:
            return (prev + curr) / 2
        else:
            return float(curr)