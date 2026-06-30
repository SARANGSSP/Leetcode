#brute force: wr count from min to mac and make an array where we store all the missing integers and return k indexed number
#if after we are done with the array and the missing array is still blank we return max + k

#optimized a lil bit: we dont need to store the missing arr we can trim down the array to the point where like  the elemnt at i index of the arr is < k - arr[i] so we start from there
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            # missing count before arr[mid]
            if arr[mid] - (mid + 1) < k:
                lo = mid + 1
            else:
                hi = mid
        # lo = number of arr elements before the kth missing number
        return lo + k