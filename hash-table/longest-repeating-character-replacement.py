class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = list(set(s))
        maxi = 0
        for char in chars:
            l = 0
            r = 0
            count = 0
            while r < len(s):
                if s[r] != char:
                    count += 1
                    r += 1
                else:
                    r+= 1
                
                while count > k:
                    if s[l] != char:
                        l += 1
                        count -= 1
                    else:
                        l += 1
                maxi = max(r-l, maxi)
        return maxi



