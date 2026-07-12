#the brute force is probabaly to go through every string and then check for max, if length is greater than max then we update max 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        string = ""
        if len(s) == 1:
            return 1
        for char in s:
            if char not in string:
                string = string + char
                maxi = max(len(string),maxi)
            elif char in string:
                maxi = max(len(string),maxi)
                dupli = string.find(char) +1
                string = string[dupli:] + char
        return maxi

        