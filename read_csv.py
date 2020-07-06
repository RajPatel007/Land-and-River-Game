import csv
import os


def readFiles():
    BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))        # get Base_dir path
    CSV_PATH = BASE_DIR + r'\resources\Task_Training_Data.csv'              # get Csv file path
    data_list = []
    with open(CSV_PATH, 'r') as csvfile:
        readingCSV = csv.reader(csvfile, delimiter=',')                     # reading csv file data
        for row in readingCSV:
            data_list.append([row[0].strip(), row[1].strip()])

    return data_list
