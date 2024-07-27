
import os
import csv

#used to import the path of the csv file to be read.
csvpath = os.path.join("Resources", "budget_data.csv")

#lists that will store the value of both rows. different values for the second column as well.

#reads the csv file
with open(csvpath, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skips the first row in the csv file.
    csv_header = next(csvreader)
    
    months = 0
    total = 0
    nex = 0
    prev = 0
    diff = 0
    months_total = []
    date = []
    

    for row in csvreader:

        months += 1

        prev =int(row[1])
        total += int(row[1])

        if (months == 1):
            nex = prev
        else:
            diff = prev - nex
            date.append(row[0])
            months_total.append(diff)
            nex = prev
    diff = round(sum(months_total)/(months - 1), 2)   

    increase = max(months_total)
    decrease = min(months_total)

    increase_date = date[months_total.index(increase)]
    decrease_date = date[months_total.index(decrease)]

with open("Analysis/Output.txt", "w") as file:

    output = (f"Financial Analysis"
               f"\n"
               f"\n-----------------------------"
               f"\n"
               f"\nTotal Months: {months}"
               f"\n"
               f"\nTotal: ${total}"
               #f"\nTotal: {"$" + (str(total))}"
               f"\n"
               f"\nAverage Change: {"$" + (str(diff))}"
               f"\n"
               f"\nThe Greatest in Increase: {increase_date} (${increase})"
               f"\n"
               f"\nThe Greatest in Increase: {decrease_date} (${decrease})"
               )
    file.write(output)
print(output)


import os
os.system("start notepad.exe Analysis/Output")