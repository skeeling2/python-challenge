#Imports I might need
import os
import csv
import statistics

#Empty lists for the data to go
BallotID = []
County = []
Candidate = []
    #Will need this empty list when trying to find candidates who got votes
UniqueCandidate = []
    #Empty list needed to add up the votes
VoteTotals = []

#Find the csv
pollcsv = os.path.join('..','PyPoll','Resources','election_data.csv')

#Read a csv
with open(pollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

#Skip the headers
    csv_header = next(csvreader)

#Put the data into the lists
    for row in csvreader:
        BallotID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
  
# Total Number of Votes Cast
VotesCast = len(Candidate)

#Each Candidate That Received Votes
for i in Candidate:
    if i not in UniqueCandidate:  
        UniqueCandidate.append(i)
#"Python Get Unique Values from a List." Geeks For Geeks, 
#https://www.geeksforgeeks.org/python-get-unique-values-list/. Accessed 12 April 2024.

#Votes That Each Candidate Received 
CCS = (Candidate.count("Charles Casper Stockham")) 
DG = (Candidate.count("Diana DeGette"))
RAD = (Candidate.count("Raymon Anthony Doane"))
#Bhadaniya, Shivali. "Count Occurances of Element in Python List. FavTutor,
#"https://favtutor.com/blogs/python-count-occurrences-in-list. Accessed 12 April 2024.

#Percentage of Votes Each Candidate Received
PercentCCS = round(CCS / VotesCast * 100, 3)
PercentDG = round(DG / VotesCast * 100, 3)
PercentRAD = round(RAD / VotesCast * 100, 3)

# Print OutPut
print()
print("Election Results")
print()
print()
print("-----------------------------")
print()
print()
print("Total Votes: " + str(VotesCast))
print()
print()
print("-----------------------------")
print()
print()
print(UniqueCandidate[0] + ":" + " " + str(PercentCCS) + "% " + "(" + str(CCS) + ")")
print()
print()
print(UniqueCandidate[1] + ":" + " " + str(PercentDG) + "% " + "(" + str(DG) + ")")
print()
print()
print(UniqueCandidate[2] + ":" + " " + str(PercentRAD) + "% " + "(" + str(RAD) + ")")
print()
print()
print("-----------------------------")
print()
print()
#Print the Winner of the Popular Vote
if CCS > DG and RAD:
    print("Winner: Charles Casper Stockham")
elif DG > CCS and RAD:
    print("Winner: Diana DeGette")
else:
    print("Winner: Raymon Anthony Doane") 
print()
print()
print("-----------------------------")


export_file = os.path.join("..","PyPoll","Analysis","PyPollResults.txt")
with open(export_file, "w") as text:
    text.write("Election Results\n\n")
    text.write("-----------------------------\n\n")
    text.write("Total Votes: " + str(VotesCast)+"\n\n")
    text.write("-----------------------------\n\n")
    text.write(UniqueCandidate[0] + ":" + " " + str(PercentCCS) + "% " + "(" + str(CCS) + ")\n\n")
    text.write(UniqueCandidate[1] + ":" + " " + str(PercentDG) + "% " + "(" + str(DG) + ")\n\n")
    text.write(UniqueCandidate[2] + ":" + " " + str(PercentRAD) + "% " + "(" + str(RAD) + ")\n\n")
    text.write("-----------------------------\n\n")
#Print the Winner of the Popular Vote
    if CCS > DG and RAD:
        text.write("Winner: Charles Casper Stockham\n\n")
    elif DG > CCS and RAD:
        text.write("Winner: Diana DeGette\n\n")
    else:
        text.write("Winner: Raymon Anthony Doane\n\n")
    text.write("-----------------------------\n\n")
#Singh, Sharika. "How to write multiple lines in text file using Python?" Tutorialspoint,
#https://www.tutorialspoint.com/How-to-write-multiple-lines-in-text-file-using-Python. Accessed 14 April 2024.
