#import modules
import os
import csv

election_path = os.path.join('Resources', 'election_data.csv')
print(election_path)

with open(election_path) as election_file:
    election_reader = csv.reader(election_file)

    candidates_list = []
        

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

        if election_list[2] not in candidates_list:
            candidates_list.append(election_list[2])


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

    percentage_list = [khan_percentage,correy_percentage,li_percentage,tooley_percentage]
    percentage_zip = zip(candidates_list,percentage_list)
    percentage_file = os.path.join('analysis', 'percentage.csv')
    #with open(percentage_file) as tally:
        #percentage_write = csv.writer(percentage_zip)
       #writer.writerow(tally)

    #print(candidates_list) 
    #print(percentage_zip)
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

election_results = os.path.join('analysis','results.txt')
with open(election_results, 'w') as results:
    print(f'Election Results', file = results)
    print(f'------------------------------',file = results)   
    print(f'Total Votes: {total_votes}', file = results)
    print(f'------------------------------', file = results)
    print(f'Khan: {round(khan_percentage,3)}% ({khan_votes})', file = results)
    print(f'Correy: {round(correy_percentage,3)}% ({correy_votes})', file = results)
    print(f'Li: {round(li_percentage,3)}% ({li_votes})', file = results)
    print(f"O'Tooley: {round(tooley_percentage,3)}% ({tooley_votes})",file = results)
    print(f'------------------------------',file = results)
    print(f'------------------------------',file = results)