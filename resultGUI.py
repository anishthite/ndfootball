#=====================footballGUI=========================
#           Author: Anish Thite
import tkinter

#init playbook
resultsgui = tkinter.Tk()
resultsgui.geometry("800x400")
resultsgui.title("Notre Dame Play Manager- Choose Play")

#define playbutton class
class playresult:
    def __init__(self,master,message, odk, rowint,col):
        button = tkinter.Button(master, text = message, bg = "light green", padx = 50, pady = 50, command = lambda: addplay(message) )
        button.grid(row = rowint, column = col, padx = 10, pady = 10)

#Defensive plays
play1 = playresult(resultsgui,"Defense", "D", 0,0)
#Kicks
play2 = playresult(resultsgui,"Kick Return", "K",  1,0)
play3 = playresult(resultsgui,"Kick Off", "K", 0,1)
#Offensive Formations
play4 = playresult(resultsgui,"Early", "O", 1,1)
play5 = playresult(resultsgui,"Late", "O", 0,2)
play6 = playresult(resultsgui,"Doubles", "O", 1,2)
resultsgui.mainloop()

