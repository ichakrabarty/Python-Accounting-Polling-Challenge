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
    
    for budget_row in budget_reader: #reads each row in csv file
        budget_list = list(budget_row)
        print(budget_list)
        
        months = months + 1
        budget_total = int(budget_list[1]) + budget_total
         
    
    print(f'Total Months: {months}') #Months in datasheet
    print(f'Total: ${budget_total}') #Total Profit/Losses

    

    
        