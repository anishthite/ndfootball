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


#playtype buttons

run = playtypebutton(resultsgui, "Run", 1,0 )
Pass = playtypebutton(resultsgui, "Pass", 2,0)
extrapt = playtypebutton(resultsgui, "Extra Pt", 3,0 )
extraPtBlock = playtypebutton(resultsgui, "Extra Pt Block", 4,0)
KO = playtypebutton(resultsgui, "KO", 5,0 )
korec = playtypebutton(resultsgui,"KO Rec", 6,0)
punt = playtypebutton(resultsgui, "Punt", 7,0)
puntrec = playtypebutton(resultsgui, "Punt Rec", 1,1)
FG = playtypebutton(resultsgui, "Fg", 2,1)
FGblock = playtypebutton(resultsgui, "FG BLock", 3,1)
twopt = playtypebutton(resultsgui, "2pt", 4,1)
twoptblock = playtypebutton(resultsgui, "2pt Block", 5,1 )
onsidekick = playtypebutton(resultsgui, "Onside Kick", 6,1)
onsidekickreturn = playtypebutton(resultsgui, "Onside Kick Rec", 7,1 )

# #playend buttons
# Batted Down
Block = playendbutton(resultsgui, "Block", 1,2)
# Blocked, Def TD
# Complete
# Complete, Fumble
# Complete, TD
# Def TD
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
# No Good
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

# play6 = playresult(resultsgui,"Doubles",  1,2)
resultsgui.mainloop()
print(playresult.playtype)
