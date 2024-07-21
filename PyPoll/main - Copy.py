import os
import csv

#used to import the path of the csv file to be read.
csvpath = os.path.join("Resource", "election_data.csv")

#lists that will store the value of the 3rd column and the quantity of each candidate to count the votes.
list_a = []
list_b = []
list_c = []
total = 0
#reads the csv file
with open(csvpath, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total = total + 1
        #updates the lists with the respected value.
        if row[2] == "Charles Casper Stockham":
                list_a.append(row[2])
        if row[2] == "Diana DeGette":
                list_b.append(row[2])
        if row[2] == "Raymon Anthony Doane":
                list_c.append(row[2])
    if len(list_a) > len(list_b) and len(list_a) > len(list_c):
        winner = list(set(list_a))
    if len(list_b) > len(list_c) and len(list_b) > len(list_a):
        winner = list(set(list_b))
    else:
        winner = list(set(str(list_c)))
        
    with open("Analysis/Output.txt", "w") as file:

        output = (f"Election Results"
                f"\n"
                f"\n-----------------------------"
                f"\n"
                f"\nTotal votes: {total}"
                f"\n"
                f"\n-----------------------------"
                f"\n"
                f"\nCharles Casper Stockham: {str(round((len(list_a))/(total)* 100, 3))}% ({str(len(list_a))})"
                f"\n"
                f"\nDiana DeGette: {str(round((len(list_b))/(total)* 100, 3))}% ({str(len(list_b))})"
                f"\n"
                f"\nRaymon Anthony Doane: {str(round((len(list_c))/(total)* 100, 3))}% ({str(len(list_c))})"
                f"\n"
                f"\n-----------------------------"
                f"\n"
                f"\nWinner: {', '.join(winner)}"
                f"\n"
                f"\n-----------------------------"
                f"\n"
            )

    
        file.write(output)
print(output)


import os
os.system("start notepad.exe Analysis/Output")