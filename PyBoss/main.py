import os
import csv

csvfile = os.path.join("employee_data.csv")

#variables
us_state_abbrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA',
    'Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI',
    'Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
    'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO',
    'Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY',
    'North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA',
    'Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT',
    'Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY',}

eID = ["Emp ID"]
fName = ["First Name"]
lName = ["Last Name"]
dob = ["DOB"]
ssn = ["SSN"]
state = ["State"]

#go through csv
with open(csvfile,newline="")as csvf:
	csvr = csv.reader(csvf,delimiter = ",")
	next(csvr)
	for row in csvr:
		eID.append(row[0])
		state.append(us_state_abbrev[row[4]])
		name = row[1].split()
		fName.append(name[0])
		lName.append(name[1])
		date = row[2].split("-")
		dob.append(date[1]+"/"+date[2]+"/"+date[0])
		number = row[3].split("-")
		ssn.append("***-**-"+number[2])
		
#combine all the individual lists into one op list
op = []
for x in range( len(eID)):
	op.append([eID[x],fName[x],lName[x],dob[x],ssn[x],state[x]])

with open("output.csv","w+") as ocsv:
	writer = csv.writer(ocsv,lineterminator="\n")
	writer.writerows(op)