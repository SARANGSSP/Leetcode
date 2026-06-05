class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        map1 , map2 = {}, {}

        for i in range(n):
            c1,c2 = s[i], t[i]
            if (c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2] != c1):
                return False
            map1[c1] = c2
            map2[c2] = c1
        return True
        


