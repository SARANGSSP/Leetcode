class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        a = sorted(hashmap.keys())
        
        half = ""
        middle = ""
        for key in a:
            count = hashmap[key]
            half += key * (count // 2)
            if count % 2 == 1:
                middle = key
        
        return half + middle + half[::-1]
