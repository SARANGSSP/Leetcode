class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        r = len(board)
        c = len(board[0])
        curr_board = []
        
        
        for i in range(r):
            row = []
            
            
            for j in range(c):
                row.append(board[i][j])
            
            
            curr_board.append(row)
        
        
        for i in range(r):
            nxt_row = i + 1
            prev_row = i - 1
            
            
            is_nxt_row_in_range = nxt_row < r
            is_prev_row_in_range = prev_row >= 0
            
            
            for j in range(c):
                live_neighbors = 0
                nxt_col = j + 1
                prev_col = j - 1
                
                
                is_nxt_col_in_range = nxt_col < c
                is_prev_col_in_range = prev_col >= 0
                
                
                if is_nxt_row_in_range:
                    live_neighbors += curr_board[nxt_row][j]
                    
                    
                    if is_prev_col_in_range:
                        live_neighbors += curr_board[nxt_row][prev_col]
                    
                    
                    if is_nxt_col_in_range:
                        live_neighbors += curr_board[nxt_row][nxt_col]
                
                
                if is_prev_row_in_range:
                    live_neighbors += curr_board[prev_row][j]
                    
                    
                    if is_prev_col_in_range:
                        live_neighbors += curr_board[prev_row][prev_col]
                    
                    
                    if is_nxt_col_in_range:
                        live_neighbors += curr_board[prev_row][nxt_col]
                
                
                if is_prev_col_in_range:
                    live_neighbors += curr_board[i][prev_col]
                
                
                if is_nxt_col_in_range:
                    live_neighbors += curr_board[i][nxt_col]
                
                
                if curr_board[i][j] == 1:
                    board[i][j] = 1 if live_neighbors == 2 or live_neighbors == 3 else 0
                else:
                    board[i][j] = 1 if live_neighbors == 3 else 0
                    


