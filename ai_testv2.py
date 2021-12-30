player, opponent = 'x', 'o'
class TTT:
    def __init__(self) -> None:
        pass
 
    def isMovesLeft(self,board) :

        for i in range(3) :
            for j in range(3) :
                if (board[i][j] == '_') :
                    return True
        return False

 
    def evaluate(self,b) :

 
        for row in range(3) :	
            if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :	
                if (b[row][0] == player) :
                    return 1
                elif (b[row][0] == opponent) :
                    return -1
 
        for col in range(3) :
        
            if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
            
                if (b[0][col] == player) :
                    return 1
                elif (b[0][col] == opponent) :
                    return -1

        if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
        
            if (b[0][0] == player) :
                return 1
            elif (b[0][0] == opponent) :
                return -1

        if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
        
            if (b[0][2] == player) :
                return 1
            elif (b[0][2] == opponent) :
                return -1

        return 0

 
    def minimax(self,board, depth, isMax) :
        score = self.evaluate(board)

 
        if (score == 1) :
            return score

 
        if (score == -1) :
            return score

 
        if (self.isMovesLeft(board) == False) :
            return 0

        if (isMax) :	
            best = -1000

            for i in range(3) :		
                for j in range(3) :
                
                    if (board[i][j]=='_') :
                    
                        board[i][j] = player

 
                        best = max( best, self.minimax(board,
                                                depth + 1,
                                                not isMax) )

                        board[i][j] = '_'
            return best

        else :
            best = 1000

            for i in range(3) :		
                for j in range(3) :
                
                    if (board[i][j] == '_') :
                    
                        board[i][j] = opponent

  
                        best = min(best, self.minimax(board, depth + 1, not isMax))

                        board[i][j] = '_'
            return best

    def findBestMove(self,board) :
        bestVal = -1000
        bestMove = (-1, -1)
 
        for i in range(3) :	
            for j in range(3) :
            
 
                if (board[i][j] == '_') :
                
 
                    board[i][j] = player

 
                    moveVal = self.minimax(board, 0, False)

    
                    board[i][j] = '_'
 
                    if (moveVal > bestVal) :			
                        bestMove = (i, j)
                        bestVal = moveVal
        # print("The value of the best Move is :", bestVal)


        print()
        return bestMove
  
  
# board = [
#         [ 'x', 'o', 'x' ],
#         [ 'o', 'o', 'x' ],
#         [ 'x', 'x', 'o' ]
#         ]

# a = TTT()

# print('player:',player)
# bestMove = a.findBestMove(board)
# print("The Optimal Move is :")
# print("ROW:", bestMove[0], " COL:", bestMove[1])


