import os
import csv

csvpath = os.path.join(".", "Profit_Loss.csv")

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

print(csvfile)