class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        string = s
        if s == goal:
            return True

        for i in range(n-1):
            s = s[1:n] + s[0]
            if s == goal:
                return True
        return False

            
