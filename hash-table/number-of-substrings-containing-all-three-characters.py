class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {'a': -1, 'b': -1, 'c': -1}
        result = 0
        for r, ch in enumerate(s):
            last[ch] = r
            result += min(last['a'], last['b'], last['c']) + 1
        return result