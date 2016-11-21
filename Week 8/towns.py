import csv
with open('towns.csv') as csvfile:
	rdr = csv.reader(csvfile)
	d = {}
	for row in rdr:
		d[row[0]] = row[1]
	for key, value in d.items():
		print(key,value)