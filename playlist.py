#csv file management python

import csv

currentgame = 'playlist.csv'

def addplay(playname):
    outputFile = open(currentgame, 'a', newline = '')
    writer = csv.writer(outputFile)
    writer.writerow([playname])
    outputFile.close()