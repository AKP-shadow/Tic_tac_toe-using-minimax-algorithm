import tkinter as tk
import ai_testv2
opp = ai_testv2.TTT()

class game_board:
    def __init__(self) -> None:
        self.board  = [
        [ '_', '_', '_' ],
        [ '_', '_', '_' ],
        [ '_', '_', '_' ]
        ]
    def current(self):
        return self.board
    def isfull(self):
        for i in self.board:
            if '_' in i:
                return False
        return True

g = game_board()
b = g.current()

    

def game_end():
    print(b)
    if g.isfull():
        if opp.evaluate(b) ==-1:
            return 'x'
        elif opp.evaluate(b) ==1:
            return 'o'
        elif opp.evaluate(b) ==0:
            return '0'

    else:
        if b[1][1]!='_':
            if b[0][0]==b[1][1]==b[2][2] :
                return b[1][1]
            elif b[0][2]==b[1][1]==b[2][0]:
                return b[1][1]

            elif b[1][1]==b[0][1]==b[2][1]:
                return b[1][1]

            elif b[1][0]==b[1][1]==b[1][2]:
    
                return b[1][1]
 
        if b[0][0]!='_':
            if b[0][0]==b[1][0]==b[2][0]:
                return b[0][0]
      
            elif b[0][0]==b[0][1]==b[0][2]:
                return b[0][0]
       
        if b[2][2]!='_':
            if b[2][0]==b[2][1]==b[2][2]:
                return b[2][2]
       
            elif b[2][2] == b[1][2] == b[0][2]:
                return b[2][2]
        
 
def best_move(): 
        move = opp.findBestMove(b)
        return move

def update_board(x,y,sym):
    b[x][y] = sym


# best_move()
    

