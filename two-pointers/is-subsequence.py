class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        i=0
        j=0
        while j< m and i < n:
            if t[i] == s[j]:
                j += 1
                i+= 1
            else:
                i+= 1
        if j == m:
            return True
        else:
            return False 

