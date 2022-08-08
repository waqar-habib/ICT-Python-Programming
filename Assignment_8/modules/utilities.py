from pandas import read_csv
import json
import sys

def get_JSON(fileDir):
    try:
        fileData = open(fileDir)
        response = json.load(fileData)
        fileData.close()

        return response
    except OSError as error:
        sys.exit(f'\n{error}.')

def get_CSV(fileDir):
    try:
        csvData = read_csv(fileDir, header = 0, sep =',')
        headers = csvData.columns
        stocks = {key: value for key, value in csvData.values}

        return stocks
    except OSError as error:
        sys.exit(f'\n{error}.')
