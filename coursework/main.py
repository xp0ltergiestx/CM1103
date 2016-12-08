import random
import csv
import itertools 
import matplotlib.pyplot as plt

def game(ra, rb):
	p = ra / (ra + rb)
	score_a = score_b = 0
	game_over = False	
	while game_over == False:			
		r = random.uniform(0, 1)
		if r < p: 
			score_a += 1
		else: 
			score_b += 1
		reached_eleven = (score_a >= 11) or (score_b >= 11)
		two_point_difference = abs(score_a-score_b) > 1
		if reached_eleven and two_point_difference: game_over = True
	return score_a, score_b

def winProbability(ra, rb, n):
	wins_a = wins_b = rallies = 0
	# rallies is initialised for question 2
	for match in range(0, n):
		score_a, score_b = game(ra, rb)
		rallies += (score_a + score_b)
		if score_a > score_b: 
			wins_a += 1
		else: 
			wins_b += 1 		
	pa = wins_a / (wins_a + wins_b) 
	pa = round(pa, 2)
	rallies = rallies / n
	# this returns the number of rallies, to help with question 2
	return pa, rallies

def englishWinProbability(ra, rb, n):
	wins_a = wins_b = rallies = 0
	for match in range(0, n):
		score_a, score_b, temp_rallies = english_game(ra, rb)
		if score_a > score_b:
			wins_a += 1
		else:
			wins_b += 1
		rallies += temp_rallies     	
	# the probability that A wins
	pa = wins_a / (wins_a + wins_b) 
	pa = round(pa, 2)
	rallies = rallies / n
	return pa, rallies

def readCSV(file):
	with open(file) as csvfile:
		rdr = csv.reader(csvfile)
		lot = []
		# This is to ignore the header row
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
	plt.title('A graph to show the probability of player A winning, against the relative abilities of the two players')
	plt.show()

def english_game(ra, rb):
	p = ra / (ra + rb)
	server = None 
	score_a = score_b = rallies = 0 
	play_to = 9
	game_over = False
	while game_over == False:			
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
		if reached_play_to: game_over = True
	return score_a, score_b, rallies

def q2():
	playerlist = readCSV('players.csv')
	eng_rallies_list = []
	rarb = []
	pars_rallies_list = []
	for key in playerlist:
		eng_rallies = englishWinProbability(key[0], key[1], 10000)[1]
		eng_rallies_list.append(eng_rallies)
		pars_rallies = winProbability(key[0], key[1], 10000)[1]
		pars_rallies_list.append(pars_rallies)
		rarb.append(key[0] / key[1])
	eng_plot, = plt.plot(rarb, eng_rallies_list)
	pars_plot, = plt.plot(rarb, pars_rallies_list)
	plt.axis([0, 10, 10, 30])
	plt.ylabel('Average time for game')
	plt.xlabel('Relative abilities Ra/Rb')
	plt.title('A graph showing relative abilities against time for rallies, for the English and PARS scoring systems')
	plt.legend([eng_plot, pars_plot], ["English Scoring System", "PARS Scoring System"])
	plt.show()

def q1e(ra, rb, min_probability):
	probabilities = {}
	probabilities['W'] = winProbability(ra, rb, 1000000)[0]
	probabilities['L'] = 1 - probabilities['W']
	total_win_probability = 0
	number_of_games = 0
	while total_win_probability < min_probability:
		number_of_games += 1	
		# these variables need to be reset each time
		total_win_probability = 0
		list_of_winning_combinations = []
		shortened_list_of_combinations = []
		final_list = []
		combinations = itertools.product('WL', repeat=((2*number_of_games)-1))
		for comb in combinations:
			wins = 0
			for j in range(0, len(comb)):
				if comb[j] == 'W':
					wins += 1
				if wins == number_of_games:
					list_of_winning_combinations.append(comb[:j+1])
		for comb in list_of_winning_combinations:
			if comb.count('W') > comb.count('L'):
				if comb[-1]  == 'W':
					shortened_list_of_combinations.append(comb)
			else:
				if i[-1] == 'L':
					shortened_list_of_combinations.append(comb)
		# removing duplicates
		final_list = set(shortened_list_of_combinations)
		for comb in final_list:
			win_prob = 1
			for char in comb:
				win_prob *= probabilities[char]  
			if comb.count('W') == number_of_games:
				total_win_probability += win_prob          
	print("To achieve a winning probability of " + str(min_probability) + " you will need to play " + str(number_of_games) + " games.")

### For question 1a uncomment the following lines:
# random.seed(57)
# print(game(70, 30))   

### For question 1b uncomment the following line:
# print(winProbability(70, 30, 1000000)[0])

### For question 1c uncomment the following line:
# print(readCSV('test.csv'))

### For question 1d uncomment the following line:
# graphMaker(readCSV('test.csv'))

### For question 1e uncomment the following line:
# q1e(60, 40, 0.9)

### For question 2 uncomment the following line:
# q2()