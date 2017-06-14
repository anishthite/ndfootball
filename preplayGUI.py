#preplay GUI
#           Author: Anish Thite
import tkinter
from playlist import addplay
#init playbook
preplaygui = tkinter.Tk()
preplaygui.geometry("800x400")
preplaygui.title("Notre Dame Play Manager- Choose Play")

#define playbutton class
class preplaytype:
    def __init__(self,master,message, odk, rowint,col):
        button = tkinter.Button(master, text = message, bg = "light green", padx = 50, pady = 50, command = lambda: addplay(message) )
        button.grid(row = rowint, column = col, padx = 10, pady = 10)

#Defensive plays
play1 = preplaytype(preplaygui,"Defense", "D", 0,0)
#Kicks
play2 = preplaytype(preplaygui,"Kick Return", "K",  1,0)
play3 = preplaytype(preplaygui,"Kick Off", "K", 0,1)
#Offensive Formations
play4 = preplaytype(preplaygui,"Early", "O", 1,1)
play5 = preplaytype(preplaygui,"Late", "O", 0,2)
play6 = preplaytype(preplaygui,"Doubles", "O", 1,2)
preplaygui.mainloop()
