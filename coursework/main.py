import random
import csv
import matplotlib.pyplot as plt

random.seed(57)

def game(ra, rb):
	# p is the probability that player A wins a point
	p = ra / (ra + rb)

	# these are the variables to store the scores for player A and B respectively
	sa = 0 
	sb = 0

	# a boolean value to determine whether the game has finished or not
	gameOver = False

	while gameOver == False:
			
		r = random.uniform(0, 1)

		if r < p:
			sa += 1
		else:
			sb += 1 

		if (sb >= 11 or sa >= 11) and (abs(sa-sb) > 1):
			gameOver = True

	return sa, sb

def winProbability(ra, rb, n):
	# initialise values for number of wins for A and B respectively
	wa = 0
	wb = 0

	for match in range(0, n):
		# sa and sb represent a and b's scores respectively 
		sa, sb = game(ra, rb)
		if sa > sb:
			wa += 1
		else:
			wb += 1	
		
	# the probability that A wins
	pa = wa / (wa + wb)	
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
	plt.plot(rarb, pa, 'bx')
	plt.axis([0, 3.5, 0, 1])
	plt.ylabel('Probability of A winning')
	plt.xlabel('Player A ability / Player B ability')
	plt.show()

# for key in readCSV('test.csv'):
# 	print(key)
# 	print(key[0], key[1])
# 	print(winProbability(key[0], key[1], 10000))




graphMaker(readCSV('test.csv'))
# print(readCSV('test.csv'))
# print(game(70, 30))	
# print(winProbability(70, 30, 100))