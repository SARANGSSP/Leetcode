class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ''.join(char.lower() for char in s if char.isalnum())
        return new_s == new_s[::-1]
