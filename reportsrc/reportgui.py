#Anish Thite
#2017
import tkinter
from simplereport import playresult
def main():
    reportgui = tkinter.Tk()    
    reportgui.geometry("1400x1000")
    reportgui.title("Notre Dame Play Manager- Analytics ")
    output = tkinter.StringVar()
    name = tkinter.StringVar()
    output.set(' v')
    name.set('')
    class computebutton:
        def __init__(self, master, message, rowint, colint, bck, output, name):
            self.button = tkinter.Button(master, text = message, bg = bck, padx =75, pady = 20, command = lambda: self.onclick(message, output, name))
            self.button.grid(row = rowint, column = colint, padx = 10, pady = 5)
            self.button.config(width = 4)
        def onclick(self, message, output, name):
            self.button.config(bg = "grey")
            name.set(message)
            if message == "Simple Most Gain":
                result = playresult('../playlist.csv')
                resultlist = result.simplemostgain()
                display = ""
                resultlist.reverse()
                for play in resultlist:
                    display += str(play)
                    display +="\n"
                output.set(display)             
          
    label1 = tkinter.Label(reportgui, text = "Compute File:", padx = 35, pady = 20 )
    label1.grid(row = 0, column = 0, padx = 5, pady = 5)
    #list buttons
    filefield = tkinter.Entry(reportgui, width = 25)
    filefield.grid(row = 0, column = 1  )
    #computebutton
    offbuttonlist = ["Simple Most Gain", "Averaged Most Gain", "Most Popular Formation (us)"]
    defbuttonlist = ["Averaged Most gain (them)", "Most Popular Formation (them)", "Most Popular Player"]
    r = 1
    index = 0
    for button in offbuttonlist:
        button = computebutton(reportgui, offbuttonlist[index] , r ,0, "light blue", output, name)
        r +=1
        index +=1
    index = 0
    for button in defbuttonlist:
        button = computebutton(reportgui, defbuttonlist[index], r,0, "light green", output, name)
        r +=1
        index +=1
    label2 = tkinter.Label(reportgui, text = "Compute File:", padx = 35, pady = 20 )
    label2.grid(row = 0, column = 2, padx = 5, pady = 5)
    
    label3 = tkinter.Label(reportgui, textvariable = output, padx = 35, pady = 20 )
    label3.grid(row = 1, column = 2, padx = 5, pady = 5)

    label4 = tkinter.Label(reportgui, textvariable = name, padx = 35, pady = 20 )
    label4.grid(row = 0, column = 3, padx = 5, pady = 5)
    reportgui.mainloop()

        
