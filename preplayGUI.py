#preplay GUI
# Anish Thite
import tkinter

def main():
#init playbook
    preplaygui = tkinter.Tk()
    preplaygui.geometry("900x1000")
    preplaygui.title("Notre Dame Play Manager- Choose PrePlay")

#DEFINE PREPLAY CLASS USED TO INOUT DATA INTO PLAYLIST.PY
    class preplay:
        def  __init__(self):
            self.down = 0
            self.distance = 0
            self.hash = ""
            self.ydline = 0
        def addDown(self,number):
            self.down = number
        def addDistance(self,number):
            self.distance += number
        def addhash(self,message):
            self.hash = message
        def addydline(self,number):
            self.ydline += number
        def multiplyydline(self,number):
            self.ydline *= number

#INITILIAZE VARIABLE TO STORE DATA
    preplay = preplay()
    class downbutton:
        def __init__(self, master, message, rowint, col):
            button = tkinter.Button(master, text = message, bg = "light green", padx = 35, pady = 20, command = lambda: preplay.addDown(message))
            button.grid(row = rowint, column = col, padx = 5, pady = 5)
            button.config(width = 5)
    class distancebutton:
        def __init__(self, master, message, rowint,col, multiplyer):
            button = tkinter.Button(master, text = message, bg = "light blue", padx = 35, pady = 20, command = lambda: preplay.addDistance((multiplyer*int(message))))
            button.grid(row = rowint, column = col, padx = 5, pady = 5)
            button.config(width = 5)
    class hashbutton:
        def __init__(self, master, message, rowint,col):
            button = tkinter.Button(master, text = message, bg = "yellow", padx = 35, pady = 20, command = lambda: preplay.addhash(message))
            button.grid(row = rowint, column = col, padx = 5, pady = 5)
            button.config(width = 5)
    class ydline:
        def __init__(self, master, message, rowint, col, multiplyer):
            button = tkinter.Button(master, text = message, bg = "light blue", padx = 35, pady = 20, command = lambda: preplay.addydline((multiplyer*int(message))))
            button.grid(row = rowint, column = col, padx = 5, pady = 5)
            button.config(width = 5)
#Down buttons
    label1 = tkinter.Label(preplaygui, text = "Down", padx = 35, pady = 20 )
    label1.grid(row = 0, column = 0, padx = 5, pady = 5)
    down = ["0","1","2","3","4"]
    r = 1
    c = 0
    for d in down:
        x = downbutton(preplaygui, d, r,c )
        r +=1
#distance buttons
    label2 = tkinter.Label(preplaygui, text = "Distance", padx = 35, pady = 20 )
    label2.grid(row = 0, column = c+1, padx = 5, pady = 5)
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    r = 1
    c +=1
    for n in numbers:
        y = distancebutton(preplaygui, n, r,c,10)
        r+=1
    r = 1
    c += 1
    for a in numbers:
        b = distancebutton(preplaygui, a,r,c,1)
        r+=1
#hash buttons
    label3 = tkinter.Label(preplaygui, text = "hash", padx = 35, pady = 20 )
    label3.grid(row = 0, column = c+1, padx = 5, pady = 5)
    hashlist = ["call","far"]
    r = 1
    c +=1
    for h in hashlist:
        v = hashbutton(preplaygui, h, r, c)
        r+=1
#ydline buttons
    label4 = tkinter.Label(preplaygui, text = "Beginning Ydline", padx = 35, pady = 20 )
    label4.grid(row = 0, column = c+1, padx = 5, pady = 5)
    r = 1
    c+=1
#10s numbers
    for i in numbers:
        u = ydline(preplaygui, i, r,c,10)
        r+=1
    r = 1
    c += 1
#1s numbers
    for q in numbers:
        w = ydline(preplaygui, q,r,c,1)
        r+=1
#neg button initilization
    negbutton = tkinter.Button(preplaygui, text = "other's", bg = "red", padx = 35, pady = 20, command = lambda: preplay.multiplyydline(-1))
    negbutton.grid(row = 1, column = c + 1, padx = 5, pady = 5)
    negbutton.config(width = 5)

#close Button
    closebutton = tkinter.Button(preplaygui, text = "Next", bg = "blue", padx = 40, pady = 20, command = preplaygui.destroy)
    closebutton.grid(row = 9, column = c +1, padx = 5, pady = 5)
    closebutton.config(width = 4)
    preplaygui.mainloop()
    return preplay

