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
    average_of_pl = 0
    total_of_differences_between_each_rows = 0
    next_row_value = 0
    
    for row in reader_as_list :
        date_column = (row[0])
        profit_and_loss_column = (row[1])
        #print(f'{date_column} {profit_and_loss_column}')
        #print(profit_and_loss_column)
        net_total_pl += int(profit_and_loss_column)
        # get the difference between this row and the last row
        differences_between_these_rows = int(profit_and_loss_column) - int(next_row_value)
        difference_list = zip(str(differences_between_these_rows))

        print(difference_list)
        next_row_value = profit_and_loss_column

        total_of_differences_between_each_rows += differences_between_these_rows
        #last_row_value = current_row_value
                
    print(f'Net total profit and loss is : {net_total_pl}')
    print(f'total of all differences : {total_of_differences_between_each_rows}')

    #calc avg of differences
    average_of_pl = total_of_differences_between_each_rows / number_of_months

    print(average_of_pl)

