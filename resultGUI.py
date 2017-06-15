#=====================footballGUI=========================
#           Author: Anish Thite
import tkinter
from playlist import addplay
#init playbook
resultsgui = tkinter.Tk()
resultsgui.geometry()
resultsgui.title("Notre Dame Play Manager- Choose Play")


#DEFINE RESULT CLASS - USED TO STORE DATA
class result:
    def __init__(self):
        self.playend = ""
        self.playtype = ""
        self.gainloss = 0
    def addPlayend(self, message):
        self.playend = message
    def addPlaytype(self,message):
        self.playtype = message
    def addGainloss(self,number):
        self.gainloss = number

#create instance of the class
playresult = result()

#define playbutton classes
class playtypebutton:

    def __init__(self,master,message, rowint,col):
        button = tkinter.Button(master, text = message, bg = "light green", padx = 40, pady = 20, command = lambda: playresult.addPlaytype(message) )
        button.grid(row = rowint, column = col, padx = 5, pady = 5)

class playendbutton:
    
    def __init__(self,master,message, rowint,col):
        button = tkinter.Button(master, text = message, bg = "light green", padx = 20, pady = 20, command = lambda: playresult.addPlayend(message) )
        button.grid(row = rowint, column = col, padx = 5, pady = 5)

class numberkeys:
    
    def __init__(self, master, message, rowint, col):
        print("placeholder")

#playtype buttons
label1 =  tkinter.Label(resultsgui, text = "Play Type", padx = 20, pady = 20 )
label1.grid(row = 0, column = 0, padx = 5, pady = 5)
play_type = ["Run","Pass", "Extra Pt", "Extra Pt Block", "KO", "KO Rec", "Punt", "PuntRec", "FG", "FG Block", "2pt", "2pt Block", "Onside Kick", "Onside Kick Rec" ]
r = 1
c = 0
for p in play_type:
    x = playtypebutton(resultsgui, p, r,c )
    r +=1
    if r > 7:
        r = 1 
        c +=1
    
#PLAYEND BUTTONS
label2 =  tkinter.Label(resultsgui, text = "Play Result", padx = 20, pady = 20 )
label2.grid(row = 0, column = 3, padx = 5, pady = 5)
play_end = ["BattedDown", "Block", "BlockedDefTD", "Complete"]
r = 1
c = 3
for i in play_end:
    j = playendbutton(resultsgui, i, r, c)  
    r +=1
    if r > 9:
        r = 1
        c+=1




#NUMKEY Buttons
label3 = tkinter.Label(resultsgui, text = "Gain/Loss", padx = 20, pady = 20)
label3.grid(row = 0, column = 3, padx = 5, pady = 5)
numbers = ["1","2","3",
           "4","5","6",
           "7","8","9",
           "0","-"
    ]

#ADD BUTTON FOR -

#POSSIBLE FUNCTIONS FOR PLAYENDS
# BattedDown = playendbutton(resultsgui, "Batted Down", 1,2)
# Block = playendbutton(resultsgui, "Block", 1,2)
# BlockedDefTD = playendbutton(resultsgui, "Blocked Def TD", 1,2)
#Complete = playendbutton(resultsgui, "Complete", 1,3)
# CompleteFumble = playendbutton(resultsgui, "Complete- Fumble", 1,2)
#CompleteTD = playendbutton(resultsgui, "Complete- TD", 2,3)
# DefTD = playendbutton(resultsgui, "Defense TD", 1,2)
# Downed
# Dropped
# Fair Catch
# Fumble
# Fumble, Def TD
# Good
# Incomplete
# Interception
# Interception, Def TD
# Interception, Fumble
#NoGood = playendbutton(resultsgui, "No Good", 3, 3)
# No Good, Def TD
# Offsetting Penalties
# Out of Bounds
# Penalty
# Penalty, Safety
# Recovered
# Return
# Rush
# Rush, Safety
# Rush, TD
# Sack
# Sack, Fumble
# Sack, Fumble, Def TD
# Sack, Safety
# Safety
# Scramble
# Scramble, TD
# Timeout
# Tipped
# Touchback

resultsgui.mainloop()
print(playresult.playtype)
