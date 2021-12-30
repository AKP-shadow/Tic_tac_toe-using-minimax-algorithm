import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import test_board
position =[
    [
[130,100,74,55],[210,100,74,54],[290,100,74,54]
    ],[
[130,160,74,54],[210,160,74,54],[290,160,74,54]
    ],[
[130,220,74,54],[210,220,74,54],[290,220,74,54]
    ]
]

class App:
    def __init__(self, root):
        self.player = 'X'
        self.root = root
        #setting title
        root.title("Tic-Tac-Toe")
        #setting window size
        width=500
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        self.box00=tk.Button(root)
        self.box00["bg"] = "#efefef"
        self.box00["fg"] = "#000000"
        self.box00["justify"] = "center"
        # self.box00["text"] = "Button"
        self.box00.place(x=130,y=100,width=74,height=54)
        self.box00["command"] = self.box00_print

        self.box01=tk.Button(root)
        self.box01["bg"] = "#efefef"
        self.box01["fg"] = "#000000"
        self.box01["justify"] = "center"
        # self.box01["text"] = "Button"
        self.box01.place(x=210,y=100,width=74,height=54)
        self.box01["command"] = self.box01_print

        self.box02=tk.Button(root)
        self.box02["bg"] = "#efefef"
        self.box02["fg"] = "#000000"
        self.box02["justify"] = "center"
        # self.box02["text"] = "Button"
        self.box02.place(x=290,y=100,width=74,height=54)
        self.box02["command"] = self.box02_print

        self.box10=tk.Button(root)
        self.box10["bg"] = "#efefef"
        self.box10["fg"] = "#000000"
        self.box10["justify"] = "center"
        # self.box10["text"] = "Button"
        self.box10.place(x=130,y=160,width=74,height=54)
        self.box10["command"] = self.box10_print

        self.box11=tk.Button(root)
        self.box11["bg"] = "#efefef"
        self.box11["fg"] = "#000000"
        self.box11["justify"] = "center"
        # self.box11["text"] = "Button"
        self.box11.place(x=210,y=160,width=74,height=54)
        self.box11["command"] = self.box11_print

        self.box12=tk.Button(root)
        self.box12["bg"] = "#efefef"
        self.box12["fg"] = "#000000"
        self.box12["justify"] = "center"
        # self.box12["text"] = "Button"
        self.box12.place(x=290,y=160,width=74,height=54)
        self.box12["command"] = self.box12_print

        self.box20=tk.Button(root)
        self.box20["bg"] = "#efefef"
        self.box20["fg"] = "#000000"
        self.box20["justify"] = "center"
        # self.box20["text"] = "Button"
        self.box20.place(x=130,y=220,width=74,height=54)
        self.box20["command"] = self.box20_print

        self.box21=tk.Button(root)
        self.box21["bg"] = "#efefef"
        self.box21["fg"] = "#000000"
        self.box21["justify"] = "center"
        # self.box21["text"] = "Button"
        self.box21.place(x=210,y=220,width=74,height=54)
        self.box21["command"] = self.box21_print

        self.box22=tk.Button(root)
        self.box22["bg"] = "#efefef"
        self.box22["fg"] = "#000000"
        self.box22["justify"] = "center"
        # self.box22["text"] = "Button"
        self.box22.place(x=290,y=220,width=74,height=54)
        self.box22["command"] = self.box22_print

    def change_player(self,player):
        self.player = player


    def opp_firstmove(self):
        pos = position[1][1]
        ft = tkFont.Font(family='Times',size=20)
        panel = tk.Label(self.root, text='O',font=ft)
        panel.place(x=pos[0],y=pos[1],width=pos[2],height=pos[3])

    def box00_print(self ):
        self.box00.destroy()
        self.open_X(pos=position[0][0])
        test_board.update_board(0,0,'X')
        self.open_O()

    def box01_print(self):
        self.box01.destroy()
        self.open_X(pos=position[0][1])
        test_board.update_board(0,1,'X')
        self.open_O()

    def box02_print(self):
        self.box02.destroy()
        self.open_X(pos=position[0][2])
        test_board.update_board(0,2,'X')
        self.open_O()

    def box10_print(self):
        self.box10.destroy()
        self.open_X(pos=position[1][0])
        test_board.update_board(1,0,'X')
        self.open_O()

    def box11_print(self):
        self.box11.destroy()
        self.open_X(pos=position[1][1])
        test_board.update_board(1,1,'X')
        self.open_O()

    def box12_print(self ):
        self.box12.destroy()
        self.open_X(pos=position[1][2])
        test_board.update_board(1,2,'X')
        self.open_O()

    def box20_print(self ):
        self.box20.destroy()
        self.open_X(pos=position[2][0])
        test_board.update_board(2,0,'X')
        self.open_O()

    def box21_print(self ):
        self.box21.destroy()
        self.open_X(pos=position[2][1])
        test_board.update_board(2,1,'X')
        self.open_O()

    def box22_print(self ):
        self.box22.destroy()
        self.open_X(pos=position[2][2])
        test_board.update_board(2,2,'X')
        self.open_O()
        # self.opponent_move()

    def iswinner(self):
        winner = test_board.game_end()
        print(winner)
        if winner:
            self.show_message(winner)
            # print(winner)
            exit

    def open_X(self,pos):
        ft = tkFont.Font(family='Times',size=20)
        panel = tk.Label(self.root, text=self.player,font=ft)
        panel.place(x=pos[0],y=pos[1],width=pos[2],height=pos[3])
        self.iswinner()
       
    def open_O(self):
        move = test_board.best_move()
        if -1 not in move:
            pos = position[move[0]][move[1]]
            # print(pos)
            # self.open_O(pos)
            print(move)
            ft = tkFont.Font(family='Times',size=20)
            panel = tk.Label(self.root, text='O',font=ft)
            panel.place(x=pos[0],y=pos[1],width=pos[2],height=pos[3])
            test_board.update_board(move[0],move[1],'O')
        self.iswinner()


    def show_message(self,winner):
        if winner=='0':
            messagebox.showinfo("Game over","Draw")
        else: 
            messagebox.showinfo("Game over",f"{winner} has won")  

    # def line_draw(self):
    #     self.canvas = tk.Canvas(self.root,width=10, height=10)
    #     self.canvas.create_line(15, 25, 200, 25)
    #     self.canvas.pack(fill = 'x', expand = True)

def start():
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    return app

 
start()
