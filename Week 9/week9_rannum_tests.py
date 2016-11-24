import MyRandom

# for i in range(5):
# 	print(MyRandom.random())

def RandExperiment(n):
	randomNumbers = []
	for i in range(n):
		currentNumber = MyRandom.random()
		randomNumbers.append(currentNumber)
	print(randomNumbers)

RandExperiment(83)		