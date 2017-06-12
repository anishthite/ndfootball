#=====================footballGUI=========================
#           Author: Anish Thite
import tkinter

#init playbook
main = tkinter.Tk()
main.geometry("800x400")
main.title("Notre Dame Play Manager- Choose Play")

#define playbutton class
class playbutton:
    def __init__(self,master,message, rowint,col):
        button = tkinter.Button(master, text = message, fg = "red", padx = 50, pady = 50 )
        button.grid(row = rowint, column = col, padx = 10, pady = 10)

play1 = playbutton(main,"Defense",0,0)
play2 = playbutton(main,"Kick Return",1,0)
play3 = playbutton(main,"Kick Off",0,1)
play4 = playbutton(main,"Early",1,1)
play5 = playbutton(main,"Late",0,2)
play6 = playbutton(main,"Doubles",1,2)
main.mainloop()
