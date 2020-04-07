import csv

def getCSVData(fileName):
    # create an empty list to store rows
    rows = []
    # Open the csv file
    dataFile = open(fileName, "r")
    # Create a CSV reader form CSV file
    reader = csv.reader(dataFile)
    # skip the header
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
