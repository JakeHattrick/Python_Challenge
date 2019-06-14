import os
import csv

csvfile = os.path.join("Resources/budget_data.csv")
#Variables
#holds values for greatest increase and decrease
dict = {"G":["Date",0],
		"L":["Date",0]}
#counter for months
months = 0
#holder for total changes
total = 0	
#empty array to hold changes
changes = []		

#go through csv
with open(csvfile,newline="")as csvf:
	csvr = csv.reader(csvf,delimiter = ",")
	next(csvr)
	previous = 0	
	for row in csvr:
		months = months+1
		total = total+int(row[1])
		change =0
		if(previous ==0):
			#if its the first row there is no change to report
			previous = int(row[1])
		else:
			change = int(row[1])-previous
			#gets the change for this month and resets previous
			previous = int(row[1])
			#adds changes to change list
			changes.append(change)
			
			#checks changes to dict holding best and worst
			if(change > int(dict["G"][1])):
				dict["G"][0] = row[0]
				dict["G"][1] = str(change)
			elif(change < int(dict["L"][1])):
				dict["L"][0] = row[0]
				dict["L"][1] = str(change)
				

print("Financial Analysis")
print("------------------------------")
print(f"Total Months :{months}")
print(f"Total: ${total}")
print("Average change: ${:.2f}".format(sum(changes)/len(changes)))
print("Greatest Increase in Profits: "+dict["G"][0]+" ($"+dict["G"][1]+")")
print("Greatest Decrease in Profits: "+dict["L"][0]+" ($"+dict["L"][1]+")")
#output
outputfile = open("Resources/output.txt","w+")

outputfile.write("Financial Analysis\n")
outputfile.write("------------------------------\n")
outputfile.write(f"Total Months :{months}\n")
outputfile.write(f"Total: ${total}\n")
outputfile.write("Average change: ${:.2f}".format(sum(changes)/len(changes))+"\n")
outputfile.write("Greatest Increase in Profits: "+dict["G"][0]+" ($"+dict["G"][1]+")\n")
outputfile.write("Greatest Decrease in Profits: "+dict["L"][0]+" ($"+dict["L"][1]+")\n")
