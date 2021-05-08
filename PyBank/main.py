#Import modules needed
import os
import csv

#Read csv file
budget_path = os.path.join( 'Resources' , 'budget_data.csv')
with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file)
    
    budget_header = next(budget_reader)
    
    months = 0 #set counter for amount of months
    budget_total = 0 #set counter for total Profit/Losses
    previous = 867884 #value of first row in csv file
    
    #counters for difference values
    total_diff = 0 
    difference = 0
    max_difference = 0
    min_difference = 0

    for budget_row in budget_reader: #reads each row in csv file
        budget_list = list(budget_row)
       
        months = months + 1
        budget_total = int(budget_list[1]) + budget_total
        
        difference =  int(budget_list[1]) - previous
        previous = int(budget_list[1])  
        
        total_diff = difference + total_diff 
    
        #Find the max and min changes in Profit/Loss
        if difference > max_difference:
            max_difference = difference
            maxvalue = max_difference
            maxmonth = budget_list[0]
        elif difference < min_difference:
            min_difference = difference
            minvalue = min_difference 
            minmonth = budget_list[0] 

    avg_diff = total_diff/(months-1) #Average Change in Profit/Loss

    print(f'Financial Analysis')
    print(f'-------------------------')
    print(f'Total Months: {months}') #Months in datasheet
    print(f'Total: ${budget_total}') #Total Profit/Losses
    print(f'Average Change: ${round(avg_diff,2)}') #Average Change in Profit/Loss
    print(f'Greatest Increase in Profits: {maxmonth} $({maxvalue})') #Max Change in Profit/Loss
    print(f'Greatest Decrease in Profits: {minmonth} $({minvalue})') #Min Change in Profit/Loss 

budget_results = os.path.join('analysis','results.txt') #txt file with results
with open(budget_results, 'w') as results:
    print(f'Financial Analysis', file = results)
    print(f'-------------------------', file = results)
    print(f'Total Months: {months}', file = results) #Months in datasheet
    print(f'Total: ${budget_total}', file = results) #Total Profit/Losses
    print(f'Average Change: ${round(avg_diff,2)}', file = results) #Average Change in Profit/Loss
    print(f'Greatest Increase in Profits: {maxmonth} $({maxvalue})', file = results) #Max Change in Profit/Loss
    print(f'Greatest Decrease in Profits: {minmonth} $({minvalue})', file = results) #Min Change in Profit/Loss

   
        