import os
import csv

#File path to the CSV file containing the data
cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Resources", "election_data.csv")

#Open CSV file and create a reader
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   

    #Skip header row
    next (csvreader)

    #Assigning a variable to count the total number of votes
    total_votes = 0

    #Looping through each row to count the total number of votes
    for row in csvreader:
        total_votes += 1
        
#Prints header as per the answer
print("\nElection Results\n")
print("---------------------------------\n")
text = ("\nElection Results\n")
text += ("---------------------------------\n")



#Prints number of total votes
print(f"Total Votes : {total_votes}\n")
print("---------------------------------\n")
text += (f"Total Votes : {total_votes}\n")
text += ("---------------------------------\n")






cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Resources", "election_data.csv")
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next (csvreader)

    #Initializing a set to store unique candidate names
    candidate_names = set()

    #Loops through each row to collect candidate names
    for row in csvreader:
        name = row[2]
        candidate_names.add(name)
    
#Converts the set of candidate names to a list, we can print this varible to get a complete list of all candidates
candidate_list = list(candidate_names)

cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Resources", "election_data.csv")
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next (csvreader)

    #Initializing a dictionary to store votes for each candidate
    votes = {}

    #Loop through each row to count votes for each candidate
    for row in csvreader:
        name = row[2]
        votes[name] = votes.get(name, 0) + 1

    #Print the vote counts and percentage using total_votes for each candidate
    for candidate, vote_count in votes.items():
        percentage = (vote_count/ total_votes) * 100
        print (f"{candidate}: {percentage: .3f}% ({vote_count})\n") 
        text += (f"{candidate}: {percentage: .3f}% ({vote_count})\n") 
        


   
    print("---------------------------------\n")
    text += ("---------------------------------\n")
    
    
    # Finding the winner based on the maximum number of votes
    winner = max(votes, key=votes.get)

    print(f"Winner: {winner}\n")
    print("---------------------------------\n")
    text += (f"Winner: {winner}\n")
    text += ("---------------------------------\n")
    


cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Analysis", "output.txt")
# with clause for write priveleges to add results in text file.
with open(csvpath, "w") as file:
    file.write(text)
print("Output file 'output.txt' created successfully!")




    




