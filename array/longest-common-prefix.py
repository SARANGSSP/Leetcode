class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        arr = sorted(strs)
        string = ""
        for i in range(len(arr[0])):
            if arr[0][i] == arr[n-1][i]:
                string = string + arr[0][i]
            else:
                break
        return(string)