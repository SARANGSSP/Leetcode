class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxi = 0
        for index,ele in enumerate(grid):
            if sum(ele) > maxi:
                maxi = sum(ele)
                maxiind = index
        return maxiind 