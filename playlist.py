#csv file management python
from resultGUI import playresult
import csv

currentgame = 'playlist.csv'

def addplay():
    outputFile = open(currentgame, 'a', newline = '')
    writer = csv.writer(outputFile)
    writer.writerow([playresult.playtype, playresult.playend, playresult.gainloss])
    outputFile.close()

addplay()