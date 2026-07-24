class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if len(s) == 1:
            return 1
        string = ""
        maxlen = 0
        for i in range(n):
            if s[i] not in string:
                string = string + s[i]
                maxlen = max(len(string),maxlen)
            else:
                index = string.find(s[i])
                string = string[index+1:]
                string += s[i]
                maxlen = max(len(string),maxlen)
        maxlen = max(len(string),maxlen)
        return maxlen

            
