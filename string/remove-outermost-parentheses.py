class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        count = 0
        out = ""
        for i in range(n):
            if s[i] == "(":
                count += 1
                if count == 1:
                    continue
                else:
                    out = out + s[i]

            elif s[i] == ")":
                count -= 1
                if count == 0:
                    continue
                else:
                    out = out + s[i]
                
        return out
                
            



             






