from pandas import read_csv
import json
import sys

# read from JSON file and return
def get_JSON(file_path):
    try:
        # open file
        data_from_file = open(file_path)
        # read data from the file as JSON
        JSON_response = json.load(data_from_file)
        # close file
        data_from_file.close()

        return JSON_response
    except OSError as error:
        sys.exit(f'\n{error}.')

# read from CSV and return rows as lists
def get_CSV(file_path):
    try:
        # import data from the csv file using
        data_from_csv = read_csv(file_path, header = 0, sep =',')
        header_list = data_from_csv.columns
        stocks_dict = {key: value for key, value in data_from_csv.values}

        return stocks_dict
    except OSError as error:
        sys.exit(f'\n{error}.')
