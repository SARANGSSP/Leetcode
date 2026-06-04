class Solution:
    def largestOddNumber(self, num: str) -> str:
        ind = -1
        s = num
        # Iterate through the string from the end to beginning
        i = 0
        for i in range(len(s) - 1, -1, -1):
            # Break if an odd digit is found
            if (int(s[i]) % 2) == 1:
                ind = i
                break
        
        # Skipping any leading zeroes
        i = 0
        while i <= ind and s[i] == '0':
            i += 1
        
        # Return the largest odd number substring
        return s[i:ind + 1]
