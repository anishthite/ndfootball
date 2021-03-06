'''resultGUI
Anish Thite 2017
creates GUI window to ask user for intouts of after-play data
'''
import tkinter
from resolution import resolution
def main():
    resultsgui = tkinter.Tk()
    resultsgui.geometry(resolution())
    resultsgui.title("Notre Dame Play Manager- Choose Result") #title of window


    #DEFINE RESULT CLASS - USED TO STORE DATA FOR USE IN PLAYLIST.PY
    class result:
        def __init__(self):
            #initializes self + variables
            self.playend = ""
            self.playtype = ""
            self.endydline = 0
            self.lastplay = False
            self.ballcarrier = 0
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
        def addBallCarrier(self, number):
            self.ballcarrier += number
    #create instance of the class for use in other classes
    playresult = result()

    #define playbutton classes
    class playtypebutton:
        def __init__(self,master,message, rowint,col):
            #initilizes button for entering data related to playtype
            self.button = tkinter.Button(master, text = message, bg = "light green", padx = 20, pady = 10, command = lambda: self.onclick(message) )
            self.button.grid(row = rowint, column = col, padx = 5, pady = 5)
            self.button.config(width = 8)
        def onclick(self, message):
            self.button.config(bg = "grey")
            playresult.addPlaytype(message)
    class playendbutton:
        def __init__(self,master,message, rowint,col):
             #initilizes button for entering data related to playtype
            self.button = tkinter.Button(master, text = message, bg = "yellow", padx = 20, pady = 10, command = lambda: self.onclick(message))
            self.button.grid(row = rowint, column = col, padx = 5, pady = 5)
            self.button.config(width = 8)
        def onclick(self, message):
            self.button.config(bg = "grey")
            playresult.addPlayend(message)
    class numberkeys:
        def __init__(self, master, message, rowint, col, multiplyer):
             #initilizes button for entering data related to endydline 
            self.button = tkinter.Button(master, text = message, bg = "light blue", padx =20, pady = 10, command = lambda: self.onclick(message, multiplyer))
            self.button.grid(row = rowint, column = col, padx = 5, pady = 5)
            self.button.config(width = 4)
        def onclick(self, message, multiplyer):
            self.button.config(bg = "grey")
            playresult.addEndYdline((multiplyer*int(message)))
    class ballcarrierkeys:
        def __init__(self, master, message, rowint, col, multiplyer):
             #initilizes button for entering data related to ball carrier
            self.button = tkinter.Button(master, text = message, bg = "green", padx =20, pady = 10, command = lambda: self.onclick(message, multiplyer))
            self.button.grid(row = rowint, column = col, padx = 5, pady = 5)
            self.button.config(width = 4)
        def onclick(self, message, multiplyer):
            self.button.config(bg = "grey")
            playresult.addBallCarrier(multiplyer*int(message))
    #playtype buttons
    #label for button
    label1 = tkinter.Label(resultsgui, text = "Play Type", padx = 20, pady = 10 )
    label1.grid(row = 0, column = 0, padx = 5, pady = 5)
    #button list
    play_type = ["Run","Pass", "Extra Pt", "Extra Pt Block", "KO", "KO Rec", "Punt", "PuntRec", "FG", "FG Block", "2pt", "2pt Block", "Onside Kick", "Onside Kick Rec" ]
    r = 1
    c = 0
    #create button
    for p in play_type:
        x = playtypebutton(resultsgui, p, r,c )
        r +=1
        if r > 10:
            r = 1 
            c +=1

    #Player Numbers
    label4 = tkinter.Label(resultsgui, text = "Ball Carrier", padx = 20, pady = 10)
    label4.grid(row = 0, column = c + 1, padx = 5, pady = 5)
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    r = 1
    c +=1
    for ones in numbers:
        d = ballcarrierkeys(resultsgui, ones, r,c,10)
        r+=1
    r = 1
    c += 1
    for tens in numbers:
        f = ballcarrierkeys(resultsgui, tens,r,c,1)
        r+=1

    #PLAYEND BUTTONS
    #label
    label2 =  tkinter.Label(resultsgui, text = "Play Result", padx = 20, pady = 10 )
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
    label3 = tkinter.Label(resultsgui, text = "End Ydline", padx = 20, pady = 20)
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
    class negbutton:
        def __init__(self, c):
            self.negbutton = tkinter.Button(resultsgui, text = "other's", bg = "red", padx = 20, pady = 20, command = lambda: self.onnegbuttonclick())
            self.negbutton.grid(row = 1, column = c + 1, padx = 5, pady = 5)
            self.negbutton.config(width = 5)        
        def onnegbuttonclick(self):
            self.negbutton.config(bg = "grey")
            playresult.multiplyGainLoss(-1)
    othersbutton = negbutton(c)
#breakloop button
    class breakButton:
        def __init__(self, c):
            self.breakbutton = tkinter.Button(resultsgui, text = "End Game", bg = "pink", padx = 40, pady = 20, command = lambda: self.onbuttonclick())
            self.breakbutton.grid(row = 9, column = c +1, padx = 5, pady = 5)
            self.breakbutton.config(width = 4)            
        def onbuttonclick(self):
            self.breakbutton.config(bg = "grey")
            playresult.lastPlay()
    stopbutton = breakButton(c)
#close window button
    closebutton = tkinter.Button(resultsgui, text = "End Play", bg = "blue", padx = 40, pady = 20, command = resultsgui.destroy)
    closebutton.grid(row = 10, column = c +1, padx = 5, pady = 5)
    closebutton.config(width = 4)

    resultsgui.mainloop()
    return playresult

