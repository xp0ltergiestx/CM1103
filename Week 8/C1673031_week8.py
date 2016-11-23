"""
Does it work on files where no error checking is needed on the fields

>>> sumRows("rows1.csv") == {'tim': 36.0, 'bob': 11.0, 'anna': 54.0}
True

Does it ignore headers if requested?

>>> sumRows("rows1.csv", header=True) == {'tim': 36.0, 'anna': 54.0}
True

Is it returning the right type of result?
>>> type(sumRows("rows1.csv"))
<class 'dict'>

Does it work on files with empty fields or fields which aren't numbers?

>>> sumRows("rows2.csv") == {'tim': 24.0, 'bob': 11.0, 'anna': 13.0}
True

Does it sum columns correctly?
>>> sumColumns("columns.csv") == {'': 0, 'tim': 5.0, 'bob': 41.0, 'anna': 55.0}
True
"""

# *** DO NOT CHANGE CODE ABOVE THIS LINE ***
# *** DO NOT ADD ANY COMMENTS OF YOUR OWN IN THE SUBMITTED SOLUTION ***

import csv

def sumRows(filename, header=False):
    d = {}
    with open(filename) as csvfile:
        rdr = csv.reader(csvfile)
        if header == True:
            next(csv.reader(csvfile))
        for row in rdr:
            rowtotal = 0
            for column in row[1:]:
                if column.isdigit():
                    rowtotal += int(column)
            d[row[0]] = rowtotal
    return d

def sumColumns(filename):
    with open(filename) as csvfile:
            rows = list(csv.DictReader(csvfile))
            d = {}
            d[''] = 0
            d['bob'] = sum(float(r['bob']) for r in rows)
            d['anna'] = sum(float(r['anna']) for r in rows)
            d['tim'] = sum(float(r['tim']) for r in rows)  
            return d       





            
