import os
import csv

#used to import the path of the csv file to be read.
csvpath = os.path.join("Resource", "election_data.csv")

#lists that will store the value of the 3rd column and the quantity of each candidate to count the votes.
list_a = []
list_b = []
list_c = []

#reads the csv file
with open(csvpath, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skips the first row in the csv file.   
    next(csvreader)

    for row in csvreader:
        #updates the lists with the respected value.
        if row[2] == "Charles Casper Stockham":
                list_a.append(row[2])
        if row[2] == "Diana DeGette":
                list_b.append(row[2])
        if row[2] == "Raymon Anthony Doane":
                list_c.append(row[2])
    #determines which list has the most amount of values that = votes and choosing the winner.           
    if len(list_a) > len(list_b) and len(list_a) > len(list_c):
        winner = list(set(list_a))
    if len(list_b) > len(list_c) and len(list_b) > len(list_a):
        winner = list(set(list_b))
    else:
        winner = list(set(str(list_c)))




      
#changes the lists into a total int value to count the votes and use in the print statement.
total_a = len(list_a)
total_b = len(list_b)
total_c = len(list_c)
total = total_a + total_b + total_c
percentage_a = (total_a / total * 100)
percentage_b = (total_b / total * 100)
percentage_c = (total_c / total * 100)

#creates a path for the output file to be put into the Analysis folder.
#all print statements will be put into the output.txt file
save_path = "Analysis"
name = ("output.txt")
txtpath = os.path.join(save_path, name)
f = open(txtpath, "w")

print("Election Results",file = f)
print("",file = f)
print("---------------------------------",file = f)
print("",file = f)
print("Total Votes:", (total),file = f)
print("",file = f)
print("---------------------------------",file = f)
print("",file = f)
print(f"Charles Casper Stockham: " +  str(round(percentage_a, 3)) + "%", "(" + str(total_a) + ")",file = f)
print("",file = f)
print("Diana Degette: "  +  str(round(percentage_b, 3)) + "%", "(" + str(total_b) + ")",file = f)
print("",file = f)
print("Raymon Anthony Doane: "  + str(round(percentage_c, 3)) + "%", "(" + str(total_c) + ")" ,file = f)
print("",file = f)
print("---------------------------------",file = f)
print("",file = f)
print(f"Winner:", (', '.join(winner)),file = f)
print("",file = f)
print("---------------------------------",file = f)

f.close()

#this will read the output file and place the data into the terminal.
with open(txtpath, "r") as f:
    data = f.read()
    print(data)