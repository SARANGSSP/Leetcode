class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""

        for ch in sorted(set(s), key=s.count, reverse=True):
            result += ch * s.count(ch)

        return result
            
        