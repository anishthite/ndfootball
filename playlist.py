#csv file management python
from preplayGUI import preplay
from playGUI import currentplay
from resultGUI import playresult
import csv

currentgame = 'playlist.csv'

def addplay():
    outputFile = open(currentgame, 'a', newline = '')
    writer = csv.writer(outputFile)
    writer.writerow([preplay.down,
                    preplay.distance,
                    preplay.hash,
                    currentplay.odk,
                    currentplay.formation,
                    playresult.playtype, 
                    playresult.playend, 
                    playresult.gainloss])
    outputFile.close()

addplay()