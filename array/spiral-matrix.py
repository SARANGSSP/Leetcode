class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Move Right along the top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1  # Move top boundary down
            
            # 2. Move Down along the right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # Move right boundary left
            
            # 3. Move Left along the bottom row (Check if row still exists)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1  # Move bottom boundary up
            
            # 4. Move Up along the left column (Check if column still exists)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1  # Move left boundary right
                
        return res