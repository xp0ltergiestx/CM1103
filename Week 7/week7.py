import csv
with open('facup.csv') as csvfile:
	rdr = csv.reader(csvfile)
	for row in rdr:
		print(row[0] + " last won in " + row[1])
		# print(type(row[1]))
		if (int(row[1]) % 2) == 0:
			print("True")
		else:
			print("False")
with open('MultipleTourWinners.csv') as csvfile:
	rdr = csv.reader(csvfile)
	for row in rdr:
		print(row[0] + " has won " + row[2] + " times.")
with open ('MultipleTourWinners.csv') as csvfile:
	rdr = csv.reader(csvfile)
	for i, row in enumerate(rdr):
		if int(row[2]) >= 3:
			print(row[0] + " has won 3 or more times.")