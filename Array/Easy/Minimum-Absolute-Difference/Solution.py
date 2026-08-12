class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #so the bruteforce I can think of is that we sort the entirity of the arr and the diff between the first two elements we take as min and then we keep reducing the mindiff if its less and pop from the array else append to the arr
        n = len(arr)
        arr.sort()
        mindiff = float(inf)
        res = []
        for i in range(n-1):
            j = i+1
            diff = arr[j] - arr[i]
            if diff < mindiff:
                while len(res) > 0:
                    res.pop()
                mindiff = diff
            if diff == mindiff:
                res.append([arr[i],arr[j]])
        return res
