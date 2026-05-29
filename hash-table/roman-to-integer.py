class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(s)
        value = 0
        i = 0
        while i < n:
            if s[i] in roman.keys():
                if i < (n-1):
                    a = roman.get(s[i])
                    b = roman.get(s[i + 1])
                    if a < b:
                        value += (b-a)
                        i += 2
                    else:
                        value += roman.get(s[i])
                        i += 1
                    
                else:
                    value += roman.get(s[i])
                    i += 1
        return value