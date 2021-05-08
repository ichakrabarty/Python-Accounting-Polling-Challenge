#import modules
import os
import csv

election_path = os.path.join('Resources', 'election_data.csv')

with open(election_path) as election_file:
    election_reader = csv.reader(election_file)

    candidates_list = [] #create list with all the candidates
        

    election_head = next(election_file)
    
    #voter counters
    total_votes = 0 
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    tooley_votes = 0

    for election_row in election_reader:
        total_votes = total_votes + 1

        election_list = list(election_row)

        if election_list[2] not in candidates_list: #puts all candidate names in candidates_list
            candidates_list.append(election_list[2])


        if election_list[2] == 'Khan':
            khan_votes = khan_votes + 1
        elif election_list[2] == 'Correy':   
            correy_votes = correy_votes + 1
        elif election_list[2] == 'Li':  
            li_votes = li_votes + 1  
        elif election_list[2] == "O'Tooley":  
            tooley_votes = tooley_votes + 1  

    #percentage of votes for each candidate
    khan_percentage = khan_votes/total_votes * 100
    correy_percentage = correy_votes/total_votes * 100
    li_percentage = li_votes/total_votes * 100
    tooley_percentage = tooley_votes/total_votes * 100

    percentage_list = [khan_percentage,correy_percentage,li_percentage,tooley_percentage]
    percentage_zip = zip(candidates_list,percentage_list)
    percentage_file = os.path.join('analysis','percentage.csv') #create new csv file with total percentages for each candidate
    with open(percentage_file, 'w', newline = '') as tally: 
        writer = csv.writer(tally)
        writer.writerow(['Name','Percent Votes'])
        writer.writerows(percentage_zip)
    with open(percentage_file, 'r') as tally2:
        tally_reader = csv.reader(tally2)
        tally_header = next(tally2)
        previous_tally = 0

        for tally_row in tally_reader:
            tally_list = list(tally_row)

            current_tally = float(tally_list[1])

            if current_tally > previous_tally: #code for winning candidate 
                max_tally = float(tally_list[1])
                winner = tally_list[0]
                
            previous_tally = float(tally_list[1])       

        
    print(f'Election Results')
    print(f'------------------------------')   
    print(f'Total Votes: {total_votes}') #prints total votes cast
    print(f'------------------------------')
    print(f'Khan: {round(khan_percentage,3)}% ({khan_votes})') #prints percentage of votes and total votes cast for khan
    print(f'Correy: {round(correy_percentage,3)}% ({correy_votes})') #prints percentage of votes and total votes cast for correy
    print(f'Li: {round(li_percentage,3)}% ({li_votes})') #prints percentage of votes and total votes cast for li
    print(f"O'Tooley: {round(tooley_percentage,3)}% ({tooley_votes})") #prints percentage of votes and total votes cast for O'Tooley
    print(f'------------------------------')
    print(f'Winner: {winner}') #prints the winner of the election
    print(f'------------------------------')

election_results = os.path.join('analysis','results.txt') #creates txt file with the results
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
    print(f'Winner: {winner}', file = results)
    print(f'------------------------------',file = results)