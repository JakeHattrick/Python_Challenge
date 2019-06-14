import os
import csv
import math

csvfile = os.path.join("Resources/election_data.csv")

#variables
votes = 0
candidates = []
candidatevotes = []

#go through csv
with open(csvfile,newline="")as csvf:
	csvr = csv.reader(csvf,delimiter = ",")
	next(csvr)
	for row in csvr:
		#ticks voter count
		votes = votes+1
		
		#if candidate is recieving first vote add to list
		if row[2] not in candidates:
			candidates.append(row[2])
			candidatevotes.append(int(0))
			
		#gives candidate their vote count	
		i = candidates.index(row[2])
		candidatevotes[i] = int(candidatevotes[i])+1

		
print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
print("--------------------------")
for candidate in candidates:
	canvotes = candidatevotes[candidates.index(candidate)]
	print(f"{candidate}: {math.ceil((canvotes/votes)*100)}% ({canvotes})")
print("--------------------------")
print(f"Winner: {candidates[candidatevotes.index(max(candidatevotes))]}")
print("--------------------------")

outputfile = open("Resources/output.txt","w+")
outputfile.write("Election Results\n")
outputfile.write("--------------------------\n")
outputfile.write(f"Total Votes: {votes}\n")
outputfile.write("--------------------------\n")
for candidate in candidates:
	canvotes = candidatevotes[candidates.index(candidate)]
	outputfile.write(f"{candidate}: {math.ceil((canvotes/votes)*100)}% ({canvotes})\n")
outputfile.write("--------------------------\n")
outputfile.write(f"Winner: {candidates[candidatevotes.index(max(candidatevotes))]}\n")
outputfile.write("--------------------------\n")