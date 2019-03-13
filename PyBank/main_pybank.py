import os
import csv

csvpath = os.path.join(".", "PyBank.csv")

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    date_column = ([0, 0])

    number_of_months = len(date_column)
                
    for row in csvreader:
        print(row)
        print(number_of_months)
    