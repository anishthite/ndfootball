#returns simple results from a game including plays with most gains and most complete
import csv

def simplemostgain():
	with open('../playlist.csv') as game:
		mostgain = csv.reader(game, delimiter = ',')
		maxgain = -100
		mostgainlist = []
		index = 0
		for play in mostgain:
			#TODO see if the play is already run, if it is then average the total gain/loss
			if int(play[9]) > maxgain:
				mostgainlist.insert(index, play)
				index +=1
	return mostgainlist
def avgmostgain():
	with open('../playlist.csv') as game:
		mostgain = csv.reader(game, delimiter = ',')
		maxgain = -100
		mostgainlist = []
		index = 0
		for play in mostgain:
			if int(play[9]) > maxgain:
				mostgainlist.insert(index, play)
				index += 1				
#def mostcomplete():


print(simplemostgain())
