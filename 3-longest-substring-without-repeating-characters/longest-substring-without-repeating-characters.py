class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxlen = 0
        string = ""
        while r < len(s):
            char = s[r]
            if char not in string:
                string = string + s[r]
                maxlen = max(len(string),maxlen)
            else:
                while char != s[l]:
                    l += 1
                l += 1
                string = s[l:r+1]
            r += 1
            maxlen = max(len(string),maxlen)
        return maxlen

            




            
