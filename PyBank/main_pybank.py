import os
import csv

csvpath = os.path.join('.', 'PyBank.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
    reader_as_list = list(csvreader)
    number_of_months = len(reader_as_list)         
    print(f'The total of months are : {number_of_months}') 
    print('---')
    
    net_total_pl = 0 

    for row in reader_as_list :
        date_column = (row[0])
        profit_and_loss_column = (row[1])
        print(date_column+' '+profit_and_loss_column)
        #print(profit_and_loss_column)

    def finding_sum() :
        profit_and_loss_total = 0
        for row in reader_as_list :
            profit_and_loss_total += profit_and_loss_column
            print(profit_and_loss_total)
           
 #   finding_sum()




