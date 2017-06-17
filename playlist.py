#csv file management python
from playGUI import currentplay
from resultGUI import playresult

import csv

currentgame = 'playlist.csv'

def addplay():
    outputFile = open(currentgame, 'a', newline = '')
    writer = csv.writer(outputFile)
    writer.writerow([currentplay.odk,currentplay.formation,playresult.playtype, playresult.playend, playresult.gainloss])
    outputFile.close()

addplay()