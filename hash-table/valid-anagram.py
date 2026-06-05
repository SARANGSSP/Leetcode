class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        string = ""
        for i in range(len(s)):
            if s[i] not in string:
                string = string + s[i]
                if s.count(s[i]) != t.count(s[i]):
                    return False
        return True