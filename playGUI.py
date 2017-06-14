#=====================footballGUI=========================
#           Author: Anish Thite
import tkinter
from playlist import addplay
#init playbook
playgui = tkinter.Tk()
playgui.geometry("800x400")
playgui.title("Notre Dame Play Manager- Choose Play")


class play:
    


currentplay = 
#define playbutton class
class playtype:
    def __init__(self,master,message, odk, rowint,col):
        button = tkinter.Button(master, text = message, bg = "light green", padx = 50, pady = 50, command = lambda: addplay(message) )
        button.grid(row = rowint, column = col, padx = 10, pady = 10)

#Defensive plays
play1 = playtype(playgui,"Defense", "D", 0,0)
#Kicks
play2 = playtype(playgui,"Kick Return", "K",  1,0)
play3 = playtype(playgui,"Kick Off", "K", 0,1)
#Offensive Formations
play4 = playtype(playgui,"Early", "O", 1,1)
play5 = playtype(playgui,"Late", "O", 0,2)
play6 = playtype(playgui,"Doubles", "O", 1,2)
playgui.mainloop()
