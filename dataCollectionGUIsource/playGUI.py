#playGUI
# creates GUI application to input data about play
# Anish Thite
import tkinter
from resolution import resolution
def main():

    playgui = tkinter.Tk()
    playgui.geometry(resolution())
    playgui.title("Notre Dame Play Manager- Choose Play")

    #CLASS USED TO STORE DATA FOR INPUT
    class play:
        def __init__(self):
            self.odk = ""
            self.formation = ""
        def addOdk(self,message):
            self.odk = message
        def addFormation(self,message):
            self.formation = message
    #create instance of the data storage class
    currentplay = play()

    #define playbuttons class
    class formationbutton:
        def __init__(self,master,message, rowint,col):
            self.button = tkinter.Button(master, text = message, bg = "light green", padx = 45, pady = 15, command = lambda: self.onclick(message))
            self.button.grid(row = rowint, column = col, padx = 5, pady = 5)
            self.button.config(width = 5)
        def onclick(self, message):
            self.button.config(bg = "grey")
            currentplay.addFormation(message)
    class odkbutton:
        def __init__(self,master,message, rowint,col):
            self.button = tkinter.Button(master, text = message, bg = "light blue", padx = 10, pady = 15, command = lambda: self.onclick(message))
            self.button.grid(row = rowint, column = col, padx = 5, pady = 5)
            self.button.config(width = 5)
        def onclick(self, message):
            self.button.config(bg = "grey")
            currentplay.addOdk(message)

    #Formation buttons initialization
    

    #ODK buttons initialization
    label2 =  tkinter.Label(playgui, text = "ODK", padx = 10, pady = 15 )
    label2.grid(row = 0, column = 0, padx = 5, pady = 5)
    play_end = ["O", "D", "K"]
    r = 1
    c =0
    #create button
    for i in play_end:
        j = odkbutton(playgui, i, r, c)  
        r +=1
        if r > 9:
            r = 1
            c+=1
    label1 = tkinter.Label(playgui, text = "Formation", padx = 10, pady = 15 )
    label1.grid(row = 0, column = c+1, padx = 5, pady = 5)
    #button list
    formations = ["Defense", "Early","Early Plus", "Late", "Late Plus", "Right", "Right Plus", "Left", "Left Plus", "Doubles Left","Doubles Left Plus",
                    "Doubles Right","Doubles Right Plus", "Open Weak Wing", "Wide Open Right", "Open","Wide Open Left Weak", 
                    "Wide Open Right Weak", "Wide Open Left Rambo Plus", "Wide Open Right Rambo Plus","Wide Open Left Rambo Minus", "Wide Open Right Rambo Minus","Wing Trey",
                    "Wing Left PLus", "Wing ", "Wing Right Plus","Wing Weak","Wing Strong", "Empty Left", "Empty Left Plus", "Empty Wing", "Empty Right Plus", "Pro","Wide Open","Trey","Trip", "Spread","Wide","Wide Wing","Wing Twins","Wing Over"]
    r = 1
    c += 1
    #create button
    for f in formations:
        x = formationbutton(playgui, f, r,c )
        r +=1
        if r > 7:
            r = 1 
            c +=1
    #close Button
    closebutton = tkinter.Button(playgui, text = "Next", bg = "blue", padx = 10, pady = 15, command = playgui.destroy)
    closebutton.grid(row = 9, column = c +1, padx = 5, pady = 5)
    closebutton.config(width = 4)
    playgui.mainloop()
    return currentplay
