import random
import csv
import matplotlib.pyplot as plt

random.seed(57)

def game(ra, rb):
	# p is the probability that player A wins a point
	p = ra / (ra + rb)

	# these are the variables to store the scores for player A and B respectively
	score_a = 0 
	score_b = 0

	# a boolean value to determine whether the game has finished or not
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
	# initialise values for number of wins for A and B respectively
	wins_a = 0
	wins_b = 0

	for match in range(0, n):
		# score_a and score_b represent a and b's scores respectively 
		score_a, score_b = game(ra, rb)
		if score_a > score_b:
			wins_a += 1
		else:
			wins_b += 1	
		
	# the probability that A wins
	pa = wins_a / (wins_a + wins_b)	
	pa = round(pa, 2)
	return pa

def readCSV(file):
	with open(file) as csvfile:
		rdr = csv.reader(csvfile)
		lot = []
		next(rdr)
		for row in rdr:
			lot.append((int(row[0]), int(row[1])))

	return lot

def graphMaker(player_list):
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

# graphMaker(readCSV('test.csv'))
# print(readCSV('test.csv'))
print(game(70, 30))	
# print(winProbability(70, 30, 100))