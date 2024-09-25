class Solution(object):
    def isPalindrome(self, x):
        string= str(x)
        rev_string = string[::-1]
        if rev_string == string:
            return True
        else:
            return False
        
        