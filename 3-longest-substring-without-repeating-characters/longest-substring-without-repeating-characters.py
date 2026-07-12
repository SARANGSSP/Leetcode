#the brute force is probabaly to go through every string and then check for max, if length is greater than max then we update max 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        maxi = 0
        for right, char in enumerate(s):
            if char in hashmap and hashmap[char] >= left:
                left = hashmap[char] + 1
            hashmap[char] = right
            maxi = max(maxi, right - left + 1)
        return maxi

        