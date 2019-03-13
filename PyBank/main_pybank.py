import os
import csv

csvpath = os.path.join(".", "PyBank.csv")

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    date_column = list(csvreader)
    number_of_months = len(date_column)         
    print(f"The total of months are : {number_of_months}") 
    