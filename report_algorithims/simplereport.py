#returns  results from a game including plays with most gains and avg
#Anish Thite 2017
import csv, sorts
def simplemostgain():
	with open('../playlist.csv') as game:
		mostgain = csv.reader(game, delimiter = ',')
		maxgain = -100
		#copy list
		mostgainlist = list(mostgain)
		sorts.quickSort(mostgainlist, 9)
	return mostgainlist
def avgmostgain():
	with open('../playlist.csv') as game:
		avgmostgain = csv.reader(game, delimiter = ',')
		maxgain = -100
		namelist = []
		avgmostgainlist = []
		playlist = list(avgmostgain)
		for play in playlist:
			found = False
			#check if the play has been listed
			for avgplay in namelist:
				if play[5] == avgplay[0]:
			#if it has then add it to the total sum, and ++ the divisor
					avgplay[1] += float(play[9])
					avgplay[2] +=1
					found = True
					break
			#if not then add it to the end of the list
			if (found == False):
				namelist.append([play[5], float(play[9]), 1])
			#divide the list into a new list
		for avgplay in namelist:
			avgmostgainlist.append([avgplay[0], (float(avgplay[1])/float(avgplay[2]))])	
			#sort 	
		sorts.quickSort(avgmostgainlist, 1)
	return avgmostgainlist					
			#if not then average it
#def mostcomplete():



	

print(avgmostgain())
