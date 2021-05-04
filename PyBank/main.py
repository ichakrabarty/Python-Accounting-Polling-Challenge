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

    for budget_row in budget_reader:
        print(budget_row)