#Anish Thite
#2017
import tkinter
from simplereport import playresult
from resolution import resolution
def main():
    reportgui = tkinter.Tk()    
    reportgui.geometry(resolution())
    reportgui.title("Notre Dame Play Manager- Analytics ")
    output = tkinter.StringVar()
    name = tkinter.StringVar()
    output.set('')
    name.set('')
    class computebutton:
        def __init__(self, master, message, rowint, colint, bck, output, name):
            self.button = tkinter.Button(master, text = message, bg = bck, padx =75, pady = 20, command = lambda: self.onclick(message, output, name))
            self.button.pack(side = "bottom")
            #self.button.grid(row = rowint, column = colint, padx = 10, pady = 5)
            self.button.config(width = 4)
        def onclick(self, message, output, name):
            #self.button.config(bg = "grey")
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
            if message == "Averaged Most Gain":             
                result = playresult('../playlist.csv')
                resultlist = result.avgmostgain('O')
                display = ""
                resultlist.reverse()
                for play in resultlist:
                    display += str(play)
                    display +="\n"
                output.set(display)
            if message == "Most Popular Formation (us)":             
                result = playresult('../playlist.csv')
                resultlist = result.mostPopularFormation('O')
                display = ""
                resultlist.reverse()
                for play in resultlist:
                    display += str(play)
                    display +="\n"
                output.set(display)
            if message == "Averaged Most Gain (them)":             
                result = playresult('../playlist.csv')
                resultlist = result.avgmostgain('D')
                display = ""
                print(resultlist.reverse())
                for play in resultlist:
                    display += str(play)
                    display +="\n"
                output.set(display)
            if message == "Most Popular Formation (them)":             
                result = playresult('../playlist.csv')
                resultlist = result.mostPopularFormation('D')
                display = ""
                resultlist.reverse()
                for play in resultlist:
                    display += str(play)
                    display +="\n"
                output.set(display)
            if message == "Most Popular Player":             
                result = playresult('../playlist.csv')
                resultlist = result.mostPopularPlayer('D')
                display = ""
                resultlist.reverse()
                for play in resultlist:
                    display += str(play)
                    display +="\n"
                output.set(display)
            if message == "Most Popular Result (them)":             
                result = playresult('../playlist.csv')
                resultlist = result.mostPopularResult('D')
                display = ""
                resultlist.reverse()
                for play in resultlist:
                    display += str(play)
                    display +="\n"
                output.set(display)
            if message == "Most Popular Result (us)":             
                result = playresult('../playlist.csv')
                resultlist = result.mostPopularResult('O')
                display = ""
                resultlist.reverse()
                for play in resultlist:
                    display += str(play)
                    display +="\n"
                output.set(display)
            if message == "Formation Analysis":             
                result = playresult('../playlist.csv')
                resultlist = result.gradeformations()
                display = ""
                resultlist.reverse()
                for play in resultlist:
                    display += str(play)
                    display +="\n"
                output.set(display)
    leftframe = tkinter.Frame(reportgui)
    leftframe.pack(side = "left")
    rightframe = tkinter.Frame(reportgui)
    rightframe.pack()
    label1 = tkinter.Label(leftframe, text = "Compute File:", padx = 35, pady = 20 )
    label1.pack(side = "top")
    #label1.grid(row = 0, column = 0, padx = 5, pady = 5)
    #list buttons
    # filefield = tkinter.Entry(leftframe, width = 25)
    # #filefield.grid(row = 0, column = 1  )
    # filefield.pack()
    #computebutton
    offbuttonlist = ["Simple Most Gain", "Averaged Most Gain", "Most Popular Formation (us)", "Formation Analysis", "Most Popular Result (us)"]
    defbuttonlist = ["Averaged Most Gain (them)", "Most Popular Formation (them)", "Most Popular Player", "Most Popular Result (them)"]
    r = 1
    index = 0
    for button in offbuttonlist:
        button = computebutton(leftframe, offbuttonlist[index] , r ,0, "light blue", output, name)
        r +=1
        index +=1
    index = 0
    for button in defbuttonlist:
        button = computebutton(leftframe, defbuttonlist[index], r,0, "light green", output, name)
        r +=1
        index +=1
    # label2 = tkinter.Label(rightframe, text = "Compute File:", padx = 35, pady = 20 )
    # label2.pack(side = "bottom")
    #label2.grid(row = 0, column = 2, padx = 5, pady = 5)
    
    label3 = tkinter.Label(rightframe, textvariable = output, padx = 35, pady = 20 )
    #label3.grid(row = 1, column = 2, padx = 5, pady = 5)
    label3.pack(side = "top")
    label4 = tkinter.Label(rightframe, textvariable = name, padx = 35, pady = 20 )
    label4.pack(side = "top")
    #label4.grid(row = 0, column = 3, padx = 5, pady = 5)
    reportgui.mainloop()

        
