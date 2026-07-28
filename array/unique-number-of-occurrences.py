class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n = len(arr)
        hashmap = {}
        for i in range(n):
            hashmap[arr[i]] = hashmap.get(arr[i],0) + 1
        freq_map = {}
        for value in hashmap.values():
            if value not in freq_map:
                freq_map[value] = 1
            else:
                return False
        return True
