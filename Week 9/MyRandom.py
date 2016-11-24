# These are the values that you must change.
m = 83
a = 84
c = 53

#You do not need to change below here
x = 57
def random():
	global x
	x = (a * x + c) % m
	return x
