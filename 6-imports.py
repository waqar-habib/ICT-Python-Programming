#Waqar Habib

#ICT 4370
#Wed, Jul 12, 2022
#Discussion 6

import csv
from tabulate import tabulate

fileName = 'ICT-Python-Programming/ICT-Python-Programming/Dogs_Week6.csv'

with open(fileName, newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    data = list(reader)
    print(data)
    print(tabulate(data))
    
# need to convert each column from csv file to a list (see ln 8) that I can use to do math operations on like caluclate weight increase etc 


