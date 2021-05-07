#Import modules needed
import os
import csv

#Read csv file
budget_path = os.path.join( 'Resources' , 'budget_data.csv')
with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file)
    print(budget_reader)
    
    budget_header = next(budget_reader)
    print(f"Header: {budget_header}")
    
    months = 0 #set counter for amount of months
    budget_total = 0 #set counter for total Profit/Losses
    previous = 867884 
    total_diff = 0
    difference = 0
    difference_copy = 0
    previous_difference = 0

    for budget_row in budget_reader: #reads each row in csv file
        budget_list = list(budget_row)
        print(budget_list)
       
        previous_difference = difference_copy
        months = months + 1
        budget_total = int(budget_list[1]) + budget_total

        
        if difference > previous_difference:
            maxvalue = difference
            maxmonth = budget_list[0]
        elif difference < previous_difference:
            minvalue = difference 
            minmonth = budget_list[0] 
        
        difference_copy = difference
        difference =  int(budget_list[1]) - previous
        previous = int(budget_list[1])  
        
        print(difference)
        total_diff = difference + total_diff 
    
    avg_diff = total_diff/(months-1)

    
    print(f'Financial Analysis')
    print(f'-------------------------')
    print(f'Total Months: {months}') #Months in datasheet
    print(f'Total: ${budget_total}') #Total Profit/Losses
    print(f'Average Change: ${round(avg_diff,2)}') #Average Change in Profit/Loss
    print(f'Greatest Increase in Profits: {maxmonth} $({maxvalue})')
    print(f'Greatest Decrease in Profits: {minmonth} $({minvalue})')

    
        