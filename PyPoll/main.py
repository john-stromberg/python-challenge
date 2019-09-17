#import dependencies 
import os
import csv

#declare csv file path
data = os.path.join("..", "Resources", "election_data.csv")

#read csv file
with open(data, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

#total votes counter, dictionary to store votes per candidates, list to store candidates, winning votes and winner values 
    total_votes = 0
    candidates_votes = {}
    candidates_list = []
    winning_votes = 0
    winner = ""
#iterate through data to add to total votes count, get names of candidates and append to list of candidates, count votes per candidates
    for rows in csv_reader:
        total_votes = total_votes + 1
        name = rows[2]
        if name not in candidates_list:
            candidates_list.append(name)
            candidates_votes[name] = 0
        candidates_votes[name] = candidates_votes[name] + 1

#determine percentage of votes won by each candidate in dictionary
    for name in candidates_votes:
        votes_per = candidates_votes.get(name)
        percentage = (float(votes_per)/float(total_votes))*100 
        voter_results = f"{name}: {percentage:.2f}% ({votes_per})"

#determine winner by vote count
        if (votes_per > winning_votes):
            winning_votes = votes_per
            winner = name

#print results 
    print("Election Results")
    print("________________________")
    print("Total Votes: " + str(total_votes))
    print("________________________")
    print(voter_results)
    print("________________________")
    print("Winner: " + str(winner))
    print("________________________")
    
#export results to text file
file = open("analysis.txt", "w")
file.write("Election Results" + "\n")
file.write("________________________" + "\n")
file.write("Total Votes: " + str(total_votes) + "\n")
file.write("________________________" + "\n")
file.write(voter_results + "\n")
file.write("_________________________" + "\n")
file.write("Winner: " + str(winner) + "\n")
file.write("_________________________")

    