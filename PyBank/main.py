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
    
    for budget_row in budget_reader: #reads each ro in csv file
        print(budget_row)
        months = months + 1
    print(f'Total Months: {months}') #Months in datasheet


    

    
        