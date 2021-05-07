#import modules
import os
import csv

election_path = os.path.join('Resources', 'election_data.csv')
print(election_path)

with open(election_path) as election_file:
    election_reader = csv.reader(election_file)

    election_head = next(election_file)
    
    #print(election_head)

    #voter counters
    total_votes = 0 
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    tooley_votes = 0

    for election_row in election_reader:
        total_votes = total_votes + 1

        election_list = list(election_row)
        candidates = []

        if election_list[2] == 'Khan':
            khan_votes = khan_votes + 1
        elif election_list[2] == 'Correy':   
            correy_votes = correy_votes + 1
        elif election_list[2] == 'Li':  
            li_votes = li_votes + 1  
        elif election_list[2] == "O'Tooley":  
            tooley_votes = tooley_votes + 1  

    khan_percentage = khan_votes/total_votes * 100
    correy_percentage = correy_votes/total_votes * 100
    li_percentage = li_votes/total_votes * 100
    tooley_percentage = tooley_votes/total_votes * 100

    print(f'Election Results')
    print(f'------------------------------')   
    print(f'Total Votes: {total_votes}')
    print(f'------------------------------')
    print(f'Khan: {round(khan_percentage,3)}% ({khan_votes})')
    print(f'Correy: {round(correy_percentage,3)}% ({correy_votes})')
    print(f'Li: {round(li_percentage,3)}% ({li_votes})')
    print(f"O'Tooley: {round(tooley_percentage,3)}% ({tooley_votes})")
    print(f'------------------------------')
    print(f'------------------------------')
