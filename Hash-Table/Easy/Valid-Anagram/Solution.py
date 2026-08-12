class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = Counter(s)
        if len(t) != len(s):
            return False
        for char in t:
            hashmap[char] = hashmap.get(char,0) -1
            if hashmap[char] < 0:
                return False
        return True

