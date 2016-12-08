import random
import csv
import itertools 
import matplotlib.pyplot as plt



def game(ra, rb):
	# setting the random seed
	# random.seed(57)

	# p is the probability that player A wins a point
	p = ra / (ra + rb)

	score_a = 0 
	score_b = 0

	gameOver = False

	while gameOver == False:
			
		r = random.uniform(0, 1)

		if r < p:
			score_a += 1
		else:
			score_b += 1

		reached_eleven = (score_a >= 11) or (score_b >= 11)
		two_point_difference = abs(score_a-score_b) > 1

		if reached_eleven and two_point_difference: gameOver = True

	return score_a, score_b

def winProbability(ra, rb, n):
	wins_a = 0
	wins_b = 0
	rallies = 0

	for match in range(0, n):
		score_a, score_b = game(ra, rb)
		rallies += (score_a + score_b)
		if score_a > score_b:
			wins_a += 1
		else:
			wins_b += 1	
		
	# the probability that A wins
	pa = wins_a / (wins_a + wins_b)	
	pa = round(pa, 2)

	rallies = rallies / n
	# this returns the number of rallies, to help with question 2
	return pa, rallies

def englishWinProbability(ra, rb, n):
	wins_a = 0
	wins_b = 0
	rallies = 0

	for match in range(0, n):
		score_a, score_b, temp = english_game(ra, rb)
		if score_a > score_b:
			wins_a += 1
		else:
			wins_b += 1
		rallies += temp		
		
	# the probability that A wins
	pa = wins_a / (wins_a + wins_b)	
	pa = round(pa, 2)
	rallies = rallies / n
	return pa, rallies

def readCSV(file):
	with open(file) as csvfile:
		rdr = csv.reader(csvfile)
		lot = []
		next(rdr)
		for row in rdr:
			lot.append((int(row[0]), int(row[1])))

	return lot

def graphMaker(player_list):
	# pa is the probability of A winning a game, rarb is As ability divided by Bs
	pa = []
	rarb = []
	for key in player_list:
		pa.append(winProbability(key[0], key[1], 10000))
		rarb.append(key[0] / key[1])	
	plt.plot(rarb, pa)
	plt.axis([0, 3.5, 0, 1])
	plt.ylabel('Probability of A winning')
	plt.xlabel('Player A ability / Player B ability')
	plt.show()

def english_game(ra, rb):

	p = ra / (ra + rb)

	server = None 

	score_a = 0 
	score_b = 0

	play_to = 9

	rallies = 0

	gameOver = False

	while gameOver == False:
			
		r = random.uniform(0, 1)

		if r < p:
			if  server == 'a':
				score_a += 1
			else:
				server = 'a'
		else:
			if server == 'b':
				score_b += 1
			else:
				server = 'b'
					

		if score_a == 8 and score_b == 8:
			if r < 0.5:
				play_to = 10	

		rallies += 1		

		reached_play_to = (score_a == play_to) or (score_b == play_to)

		if reached_play_to: gameOver = True

	return score_a, score_b, rallies

def q2():
	playerlist = readCSV('players.csv')
	eng_pa_list = []
	eng_rallies_list = []
	rarb = []
	pars_pa_list = []
	pars_rallies_list = []
	for key in playerlist:
		eng_pa, eng_rallies = englishWinProbability(key[0], key[1], 10000)
		eng_pa_list.append(eng_pa)
		eng_rallies_list.append(eng_rallies)

		pars_pa, pars_rallies = winProbability(key[0], key[1], 10000)
		pars_pa_list.append(pars_pa)
		pars_rallies_list.append(pars_rallies)
		rarb.append(key[0] / key[1])

	plt.plot(rarb, eng_rallies_list)
	plt.plot(rarb, pars_rallies_list)
	plt.axis([0, 10, 10, 30])
	plt.ylabel('Average time for game')
	plt.xlabel('Relative abilities Ra/Rb')
	plt.title('A graph showing relative abilities against time for rallies, for the English and PARS scoring systems')
	plt.show()

def q1e(ra, rb, minProbability):
	probabilities = {}
	probabilities['W'] = winProbability(ra, rb, 1000000)[0]
	probabilities['L'] = 1 - probabilities['W']
	
	totalwinprobability = 0
	numberOfGames = 0
	

	while totalwinprobability < minProbability:
		numberOfGames += 1
		
		# these variables need to be reset each time
		totalwinprobability = 0
		listOfWinningCombinations = []
		shortenedListOfCombinations = []
		finalList = []

		combinations = itertools.product('WL', repeat=((2*numberOfGames)-1))

		for comb in combinations:
			wins = 0
			for j in range(0, len(comb)):
				if comb[j] == 'W':
					wins += 1
				if wins == numberOfGames:
					listOfWinningCombinations.append(comb[:j+1])

		for comb in listOfWinningCombinations:
			if comb.count('W') > comb.count('L'):
				if comb[-1]  == 'W':
					shortenedListOfCombinations.append(comb)
			else:
				if i[-1] == 'L':
					shortenedListOfCombinations.append(comb)

		# removing duplicates
		finalList = set(shortenedListOfCombinations)

		for comb in finalList:
			winProb = 1
			for char in comb:
				winProb *= probabilities[char]	
			if comb.count('W') == numberOfGames:
				totalwinprobability += winProb			
				

	print("To achieve a winning probability of " + str(minProbability) + " you'll need to play " + str(numberOfGames) + " games.")


### For question 1a, uncomment the random seed in the 'game' function, and the following line:
# print(game(70, 30))	

### For question 1b, uncomment the following line, and make sure the random seed in 'game' is not set:
# print(winProbability(70, 30, 1000000))

### For question 1c, uncomment the following line:
# print(readCSV('test.csv'))

### For question 1d, make sure random seed is not set and uncomment the following line:
# graphMaker(readCSV('test.csv'))

### For question 1e, make sure random seed is not set and uncomment the following line:
# q1e(60, 40, 0.9)

### For question 2, make sure random seed is not set and uncomment the following line:
# q2()

