'''resultGUI
Anish Thite 2017
creates GUI window to ask user for intouts of after-play data
'''
import tkinter
def main():
    resultsgui = tkinter.Tk()
    resultsgui.geometry("1400x1000")
    resultsgui.title("Notre Dame Play Manager- Choose Result") #title of window


    #DEFINE RESULT CLASS - USED TO STORE DATA FOR USE IN PLAYLIST.PY
    class result:
        def __init__(self):
            #initializes self + variables
            self.playend = ""
            self.playtype = ""
            self.endydline = 0
            self.lastplay = False
        def addPlayend(self, message):#modifier
            self.playend = message
        def addPlaytype(self, message):#modifier
            self.playtype = message
        def addEndYdline(self, number):#modifier
            self.endydline += number
        def multiplyGainLoss(self, number):#modifier
            self.endydline *= number
        def lastPlay(self):
            self.lastplay = True
    #create instance of the class for use in other classes
    playresult = result()

    #define playbutton classes
    class playtypebutton:
        def __init__(self,master,message, rowint,col):
            #initilizes button for entering data related to playtype
            button = tkinter.Button(master, text = message, bg = "light green", padx = 40, pady = 20, command = lambda: playresult.addPlaytype(message))
            button.grid(row = rowint, column = col, padx = 5, pady = 5)
            button.config(width = 10)

    class playendbutton:
        def __init__(self,master,message, rowint,col):
             #initilizes button for entering data related to playtype
            button = tkinter.Button(master, text = message, bg = "yellow", padx = 35, pady = 20, command = lambda: playresult.addPlayend(message) )
            button.grid(row = rowint, column = col, padx = 5, pady = 5)
            button.config(width = 10)
    class numberkeys:
        def __init__(self, master, message, rowint, col, multiplyer):
             #initilizes button for entering data related to endydline 
            button = tkinter.Button(master, text = message, bg = "light blue", padx =35, pady = 20, command = lambda: playresult.addEndYdline((multiplyer*int(message))))
            button.grid(row = rowint, column = col, padx = 5, pady = 5)
            button.config(width = 5)

    #playtype buttons
    #label for button
    label1 = tkinter.Label(resultsgui, text = "Play Type", padx = 35, pady = 20 )
    label1.grid(row = 0, column = 0, padx = 5, pady = 5)
    #button list
    play_type = ["Run","Pass", "Extra Pt", "Extra Pt Block", "KO", "KO Rec", "Punt", "PuntRec", "FG", "FG Block", "2pt", "2pt Block", "Onside Kick", "Onside Kick Rec" ]
    r = 1
    c = 0
    #create button
    for p in play_type:
        x = playtypebutton(resultsgui, p, r,c )
        r +=1
        if r > 7:
            r = 1 
            c +=1
    
    #PLAYEND BUTTONS
    #label
    label2 =  tkinter.Label(resultsgui, text = "Play Result", padx = 35, pady = 20 )
    label2.grid(row = 0, column = c+1, padx = 5, pady = 5)
    play_end = ["BattedDown", "Block", "BlockedDefTD", "Complete","CompleteFumble","CompleteTD","DefTD", "Downed","Dropped","Fair Catch","Fumble","Fumble, Def TD","Good",
"Incomplete","Interception","Interception, Def TD","Interception, Fumble",
"NoGood", "No Good, Def TD","Offsetting Penalties","Out of Bounds","Penalty","Penalty, Safety","Recovered","Return",
"Rush","Rush, Safety","Rush, TD","Sack","Sack, Fumble","Sack, Fumble, Def TD","Sack, Safety","Safety","Scramble","Scramble, TD","Timeout","Tipped","Touchback"]
    r = 1
    c +=1
    #create button
    for i in play_end:
        j = playendbutton(resultsgui, i, r, c)  
        r +=1
        if r > 10:
            r = 1
            c+=1




#NUMKEY Buttons
    label3 = tkinter.Label(resultsgui, text = "End Ydline", padx = 35, pady = 20)
    label3.grid(row = 0, column = c+1, padx = 5, pady = 5)
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    r = 1
    c +=1
    for x in numbers:
        y = numberkeys(resultsgui, x, r,c,10)
        r+=1
    r = 1
    c += 1
    for a in numbers:
        b = numberkeys(resultsgui, a,r,c,1)
        r+=1
#NEGATIVE BUTTON
    negbutton = tkinter.Button(resultsgui, text = "neg", bg = "red", padx = 35, pady = 20, command = lambda: playresult.multiplyGainLoss(-1))
    negbutton.grid(row = 1, column = c + 1, padx = 5, pady = 5)
    negbutton.config(width = 5)

#POSSIBLE FUNCTIONS FOR PLAYENDS


#breakloop button
    breakbutton = tkinter.Button(resultsgui, text = "End Game", bg = "pink", padx = 40, pady = 20, command = playresult.lastPlay)
    breakbutton.grid(row = 9, column = c +1, padx = 5, pady = 5)
    breakbutton.config(width = 4)
#close window button
    closebutton = tkinter.Button(resultsgui, text = "End Play", bg = "blue", padx = 40, pady = 20, command = resultsgui.destroy)
    closebutton.grid(row = 10, column = c +1, padx = 5, pady = 5)
    closebutton.config(width = 4)

    resultsgui.mainloop()
    return playresult

