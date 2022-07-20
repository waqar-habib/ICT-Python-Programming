#Waqar Habib

#ICT 4370
#Wed, Jul 12, 2022
#Discussion 6

import csv
from tabulate import tabulate

fileName = 'ICT-Python-Programming/ICT-Python-Programming/Dogs_Week6.csv'

names = []
weights = []
increaseYr1 = []
increaseYr2 = []

with open(fileName) as csvFile:
    csvFile.readline() # Skip header line
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        names.append(row[0])
        weights.append(row[1])
print(names)
print(weights)


