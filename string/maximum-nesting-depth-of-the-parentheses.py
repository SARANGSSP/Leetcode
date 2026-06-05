class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        counter = 0
        maxi = 0
        for char in s:
            if char == "(":
                counter += 1
            elif char == ")":
                counter -= 1
            maxi = max(maxi,counter)
        return(maxi)