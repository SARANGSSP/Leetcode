class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        row_check = 0
        for i in range(row):
            if matrix[i][0] <= target:
                row_check += 1
                print(row_check)
            else:
                break

        for i in range(column):
            if matrix[row_check-1][i] == target:
                return True
        return False
        
