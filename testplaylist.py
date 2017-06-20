import playlist

breakFlag = False
while breakFlag == False:
    newplay = playlist.playlist()
    newplay.addplay('playlist.csv')
    if (newplay.playresult.lastplay == True) :
        breakFlag = True
    