from tkinter import *

root = Tk()
root.title("TIC TAC TOE")

text = Entry(root, font = ("calibri", 16))
text.pack(fill = X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player = "X"
button = []
stop_game = False
stop_game_tie = False

def Game_Over():
    Check_Winner()
    Check_Tie()

    if stop_game == True:
        Hplayer()
        text.delete(0, END)
        text.insert(0, "'{}' WINNER".format(player))

    if stop_game_tie == True:
        text.delete(0, END)
        text.insert(0, "TIE MATCH")

def Check_Winner():
    global stop_game
    
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        stop_game = True

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        stop_game = True

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        stop_game = True

def Check_Tie():
    global stop_game_tie

    if "-" not in board:
        stop_game_tie = True


def Hplayer():
    global player

    if player == "X":
        player = "O"
    
    else:
        player = "X"

def Add_Text(pos, play):
    global button
    if pos not in button and stop_game == False and stop_game_tie == False:
    
        if pos == 0:
            button_1.configure(text = play)
            board[0] = player

        elif pos == 1:
            button_2.configure(text = play)
            board[1] = player
        
        elif pos == 2:
            button_3.configure(text = play)
            board[2] = player
        
        elif pos == 3:
            button_4.configure(text = play)
            board[3] = player
        
        elif pos == 4:
            button_5.configure(text = play)
            board[4] = player
        
        elif pos == 5:
            button_6.configure(text = play)
            board[5] = player
        
        elif pos == 6:
            button_7.configure(text = play)
            board[6] = player
        
        elif pos == 7:
            button_8.configure(text = play)
            board[7] = player
        
        else:
            button_9.configure(text = play)
            board[8] = player
        
        button.append(pos)
        Hplayer()
        Game_Over()

# GRID

frame = Frame(root)
frame.pack(side = TOP, anchor = NW)

frame1 = Frame(frame)
frame1.pack()

button_1 = Button(frame1, text = "", width = 9, height = 3, command = lambda:Add_Text(0, player))
button_1.pack(side = LEFT)

button_2 = Button(frame1, text = "", width = 9, height = 3, command = lambda:Add_Text(1, player))
button_2.pack(side = LEFT)

button_3 = Button(frame1, text = "", width = 9, height = 3, command = lambda:Add_Text(2, player))
button_3.pack(side = LEFT)

frame2 = Frame(frame)
frame2.pack()

button_4 = Button(frame2, text = "", width = 9, height = 3, command = lambda:Add_Text(3, player))
button_4.pack(side = LEFT)

button_5 = Button(frame2, text = "", width = 9, height = 3, command = lambda:Add_Text(4, player))
button_5.pack(side = LEFT)

button_6 = Button(frame2, text = "", width = 9, height = 3, command = lambda:Add_Text(5, player))
button_6.pack(side = LEFT)

frame3 = Frame(frame)
frame3.pack()

button_7 = Button(frame3, text = "", width = 9, height = 3, command = lambda:Add_Text(6, player))
button_7.pack(side = LEFT)

button_8 = Button(frame3, text = "", width = 9, height = 3, command = lambda:Add_Text(7, player))
button_8.pack(side = LEFT)

button_9 = Button(frame3, text = "", width = 9, height = 3, command = lambda:Add_Text(8, player))
button_9.pack(side = LEFT)

root.mainloop()