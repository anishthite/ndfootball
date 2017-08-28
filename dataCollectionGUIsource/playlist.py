#csv file management python
import preplayGUI 
import playGUI
import resultGUI
import csv



class playlist:
    def __init__(self):
        self.preplay = preplayGUI.main()
        self.currentplay = playGUI.main()
        self.playresult = resultGUI.main()
    def computeGainLoss(self):
        beg = int(self.preplay.ydline)
        end = int(self.playresult.endydline)
        
        #if beg ydline is +
        if beg > 0:
            #if end ydline > 0
            if int(end) > 0: #both +
                return beg-end
            else: # beg +, end -
                return (-1 *(50-abs(end)) + (beg-50))
        else:
            #if end ydline > 0
            if int(end) > 0: # beg -, end +
                return ((50-abs(beg)) + (50-end))
            else: # both -
                return abs(end) - abs(beg)

    def addplay(self,currentgame):
        outputFile = open(currentgame,'a',newline = '')
        writer = csv.writer(outputFile)
        writer.writerow([
                    self.preplay.down,
                    self.preplay.distance,
                    self.preplay.hash,
                    self.preplay.ydline,
                    self.currentplay.odk,
                    self.currentplay.formation,
                    self.playresult.playtype, 
                    self.playresult.playend, 
                    self.playresult.endydline,
                    self.computeGainLoss(),
                    self.playresult.ballcarrier
                    ])
        outputFile.close()