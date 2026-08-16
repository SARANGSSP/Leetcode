class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxi = 0
        for index,ele in enumerate(grid):
            if sum(ele) == n-1:
                return index
