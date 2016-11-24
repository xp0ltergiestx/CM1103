# These are the values that you must change.
m = 87
a = 21
c = 57

#You do not need to change below here
x = 57
def random():
	global x
	x = (a * x + c) % m
	return x
