class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        arr = [[0 for i in range(3)]for i in range(3)]
        n = len(moves)
        turn = 2
        for ele in moves:
            if turn % 2 == 0:
                arr[ele[0]][ele[1]] = 1
            else:
                arr[ele[0]][ele[1]] = -1
            turn += 1
        print(arr)
        #Check for rows
        for ele in arr:
            if sum(ele) == 3:
                return ("A")
            elif sum(ele) == -3:
                return("B")
        #check for columns
        for i in range(3):
            colsum = 0
            for j in range(3):
                colsum += arr[j][i]
            if colsum == 3:
                return ("A")
            if colsum == -3:
                return ("B")
        
        #check for diagonals:
        diag1sum = 0
        diag2sum = 0
        for i in range(3):
                diag1sum += arr[i][i]
                diag2sum += arr[i][2-i]
        if diag1sum == 3 or diag2sum == 3:
            return ("A")
        if diag1sum == -3 or diag2sum == -3:
            return ("B")

        if len(moves) == 9:
            return("Draw")
        else:
            return("Pending")              

                
            
            
            
