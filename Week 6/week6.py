# question 1
sports = ["football", "rugby", "hockey", "tennis"]
print(sports[0] + " " + sports[-1])
sports.append("cycling")
print(len(sports))
for item in sports:
	print(item[0])
sports.remove("football")
new_list = sports[1:-1]	

# question 2
letters = ['a', 'b', 'c', 'd', 'e']
letters.remove(letters[3])
letters.remove('a')

# question 5
a = ["tim", "bob", "trevor", "susan", "anna"]
vowels = ['a', 'e', 'i', 'o', 'u']
print(sorted(a, key=lambda x : x[0]))
print(sorted(a, key=lambda x : x[1]))
print(sorted(a, key=lambda x : x[:-1]))
print(sorted(a, key=lambda x : len(x)))
print(sorted(a, key=lambda x : (len(x), x[0])))
print(sorted(a, key=lambda x : x if x[0] in vowels else x[0]))

# question 6
def print_square(m, n):
	for y in range(n):
		for x in range(m):
			print("*", end="")
		print()	
print_square(20, 20)

# question 7
def load_pallets(weight_list):
	current_weight = 0
	x = 0
	while current_weight <= 3000:
		if (current_weight + weight_list[x]) <= 3000:
			current_weight += weight_list[x]
			x += 1
		else: 
			break	
	print(current_weight)
weights = [ 750, 387, 291, 712, 100, 622, 109, 750, 282 ]	
load_pallets(weights)	

# question 8
def print_square_with_inputs():
	print("Enter your desired width:")
	m = int(input())
	print("Enter your desired height:")
	n = int(input())
	for y in range(n):
		for x in range(m):
			print("*", end="")
		print()

# question 9
A = set([1, 2, 3, 4])
B = set([3, 4, 5, 6])
print(A | B)
print(A & B)
print(A - B)
print((A-B) | (B - A))
print(A & A)

