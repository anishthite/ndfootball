#returns  results from a game including plays with most gains and avg
#Anish Thite 2017
import csv, sorts

class playresult:
	global csvlocation, game, gamefile
	def __init__(self, csvloc):
		self.csvlocation = csvloc
		self.gamefile = open(self.csvlocation)
		self.game = list(csv.reader(self.gamefile, delimiter = ','))
	def splitlist(self, ndrole):
		parsedplays = []
		#put all O or D in teamside
		for play in self.game:
			if play[4] == ndrole:
				parsedplays.append(play)
		return parsedplays
	#Offensive Analysis
	# def fliplist(self, oldlist):
	# 		newlist = []
	# 		index = oldlist.length - 1
	# 		for  x in range :
					
	def simplemostgain(self):
			maxgain = -100
			#copy list
			plays = self.splitlist('O')
			sorts.quickSort(plays, 9)

			return plays
	def avgmostgain(self, ndrole):
			namelist = []
			avgmostgainlist = []
			for play in self.splitlist(ndrole):
				found = False
				#check if the play has been listed
				for avgplay in namelist:
					if play[5] == avgplay[0] and play[6] == avgplay[1]:
				#if it has then add it to the total sum, and ++ the divisor
						avgplay[2] += float(play[9])
						avgplay[3] +=1
						found = True
						break
				#if not then add it to the end of the list
				if (found == False):
					namelist.append([play[5], play[6], float(play[9]), 1])
				#divide the list into a new list
			for avgplay in namelist:
				avgmostgainlist.append([[avgplay[0], avgplay[1]], (float(avgplay[2])/float(avgplay[3]))])	
				#sort 	
			sorts.quickSort(avgmostgainlist, 1)
			return avgmostgainlist						
				#if not then average it
	#off and def
	def mostPopularFormation(self, ndrole):
		parsedplays = []
		popularplay = []
		#put all O or D in teamside
		for play in self.splitlist(ndrole):
			parsedplays.append([play[5], play[6]])	
		#for each play in parsedplays
		for play in parsedplays:	
			found = False
			#if game is in popform list add one to obj type
			for countedplay in popularplay:
				if play == countedplay[0]:
					countedplay[1] +=1
					found = True
					break
			if (found == False):
				popularplay.append([play, 1])
		#return popform list 
		sorts.quickSort(popularplay, 1)
		return popularplay
	# #def
	def mostPopularPlayer(self, ndrole):
		parsedplays = []
		popularplayer = []
		#put all O or D in teamside
		for play in self.splitlist(ndrole):
				parsedplays.append([play[5], play[10]])
		for play in parsedplays:	
			found = False
			#if game is in popform list add one to obj type
			for countedplay in popularplayer:
				if play[0] == countedplay[0] and play[1] == countedplay[1]:
					countedplay[2] +=1
					found = True
					break
			if (found == False):
				popularplayer.append([play[0], play[1], 1])
		#return popform list 
		sorts.quickSort(popularplayer, 2)
		return popularplayer
	# #off and def
	#UP NEXT ==========================================================
	def mostPopularResult(self, ndrole):
		parsedplays = []
		resultplay = []
		#put all O or D in teamside
		for play in self.splitlist(ndrole):
			parsedplays.append([play[5], play[6]])	
		#for each play in parsedplays
		for play in parsedplays:	
			found = False
			#if game is in popform list add one to obj type
			for countedplay in resultplay:
				if play[0] == countedplay[0] and play[1] == countedplay[1]:
					countedplay[2] +=1
					found = True
					break
			if (found == False):
				resultplay.append([play[0],play[1], 1])
		#return popform list 
		sorts.quickSort(resultplay, 2)
		return resultplay
	def searchindexplaylist(self,name,list):
		index = 1
		for play in list:
			if play[0] == name:
				return index
				break 
			else:
				index +=1
			
	def gradeformations(self):    #idea: match rankings
		parsedplays = []
		gradedformations = []
		# for play in self.splitlist('O'):
		# 		parsedplays.append(play)
		# for play in parsedplays:
		for play in self.avgmostgain('O'):
			avgindex = self.searchindexplaylist(play[0], self.avgmostgain('O'))
			runindex = self.searchindexplaylist(play[0],self.mostPopularFormation('O'))
			if runindex/avgindex > 1:
				gradedformations.append([play[0], "RUN LESS", runindex/avgindex ])
			elif runindex/avgindex < 1:
				gradedformations.append([play[0], "RUN MORE", runindex/avgindex])
			else:
				gradedformations.append([play[0], "NO CHANGE", runindex/avgindex])
		sorts.quickSort(gradedformations,2)
		return gradedformations	
	#defmostPopularOutcome
		#run v pass


#def weightcompleteness(play):


	# 		if []
		#if complete is equal to certain string
		#return new list [name, completeness, weightage]
	#def mostcomplete():



	

