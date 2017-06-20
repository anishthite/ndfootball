#csv file management python
from preplayGUI import preplay
from playGUI import currentplay
from resultGUI import playresult
import csv

currentgame = 'playlist.csv'

def computeGainLoss():
    beg = int(preplay.ydline)
    end = int(playresult.endydline)
    
    #if beg ydline is +
    if beg > 0:
        #if end ydline > 0
        if int(end) > 0: #both +
            return beg-end
        else: # beg +, end -
            return ((50-abs(end)) + (50-beg))
    else:
        #if end ydline > 0
        if int(end) > 0: # beg -, end +
            return ((50-abs(beg)) + (50-end))
        else: # both -
            return abs(end) - abs(beg)




computeGainLoss()


def addplay():
    outputFile = open(currentgame, 'a', newline = '')
    writer = csv.writer(outputFile)
    writer.writerow([preplay.down,
                    preplay.distance,
                    preplay.hash,
                    preplay.ydline,
                    currentplay.odk,
                    currentplay.formation,
                    playresult.playtype, 
                    playresult.playend, 
                    playresult.endydline])
    outputFile.close()

addplay()