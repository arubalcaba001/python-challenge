#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv

filepath =os.path.join("..","PyPoll","election_data.csv")

#Set all of the holders and read the csv files

TotalVoters=[]
Voters=[]
VotersCandidate=[]
Candidate=[]
TotCount=[]
CandidatePercentage=[]
Results=[]

with open ("election_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    csvheader=next(csvreader) #Will skip the header
    for row in csvreader: 
        Voters.append(row[0]) #append will hold the values you asked the for to do
        VotersCandidate.append(row[2]) # append will hold the list of candidate and the number of times people voted

TotalVoters=len(Voters)

for x in set(VotersCandidate):
    Candidate.append(x) #do tuple and sort by the second sorted(candidates, key=lamba pair: pair=1 reverse=True)
    y=VotersCandidate.count(x)
    TotCount.append(y)
    z=(y/TotalVoters)*100
    CandidatePercentage.append(z)
 
    WinnerCount = max(TotCount)
    Winner = Candidate[TotCount.index(WinnerCount)]
 
print("Election Results")
print("=================================")
print("Total Votes: " +str(TotalVoters))
print("=================================")


for i in range(len(TotCount)):
    print (str(Candidate[i]) + ":  "+ str(round(CandidatePercentage[i],3))+"%  " +str(TotCount[i]))

print("=================================")
print("Winner:  " +Winner)
print("=================================")

#Output to a text file
NewFile = open("PyPoll.txt","w")
NewFile.write("Election Results"+"\n")
NewFile.write("================================="+"\n")
NewFile.write("Total Votes: " +str(TotalVoters)+"\n")
NewFile.write("================================="+"\n")

for i in range(len(TotCount)):
    NewFile.write(str(Candidate[i]) + ":  "+ str(round(CandidatePercentage[i],3))+"%  " +str(TotCount[i])+"\n")

NewFile.write("================================="+"\n")
NewFile.write("Winner:  " +Winner)
NewFile.write("================================="+"\n")

NewFile.close()