#Waqar Habib

#ICT 4370
#Wed, Jul 12, 2022
#Discussion 6

import csv

fileName = 'ICT-Python-Programming/ICT-Python-Programming/Dogs_Week6.csv'
# open the file in read mode
filename = open(fileName, 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
dog = []
weight = []
 
# iterating over each row and append
# values to empty list
for col in file:
    dog.append(col['Dog'])
    weight.append(col['Weight'])
    # totalunit.append(col['total_units'])
 
# printing lists
print('Dog:', dog)
print('Weight:', weight)
