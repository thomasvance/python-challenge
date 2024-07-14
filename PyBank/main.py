
import os
import csv

#used to import the path of the csv file to be read.
csvpath = os.path.join("Resources", "budget_data.csv")

#lists that will store the value of both rows. different values for the second column as well.
profit = []
average = []
diff = {}
prev = 0
nex = 0
total = 0
#reads the csv file
with open(csvpath, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skips the first row in the csv file.
    next(csvreader)
    


    

    for row in csvreader:

        #sets nex as the first value in the row. Will not be put into a list, 
        #but will be used to find the difference between it and the next row.
        nex = int(row[1])

        #prev starts at 0 so it skips the first row to calculate the absolute difference.
        if prev == 0:
            pass
        else:
            #this compares the absolute value between the prev and nex, if nex is a negative,
            #and prev is a positive, it will calculate the absolute value as a negative decrease.
            if prev > nex and int(row[1]) < 0:
                inc = (abs(prev - nex))
                diff.update({row[0]: -inc})
                average.append(-inc)
                
            #this compares the absolute value between the prev and nex, if nex is a positive,
            #and prev is a positive, but nex is bigger it will calculate the absolute value as a positive increase.
            if prev < nex and int(row[1]) > 0:
                inc = (abs(prev - nex))
                diff.update({row[0]: inc})
                average.append(inc)
                
            #this compares the absolute value between the prev and nex, if prev is greater than nex,
            #and nex is positive, but nex is smaller then it will be a postive decrease.
            if prev > nex and int(row[1]) > 0:
                inc = (abs(prev - nex))
                diff.update({row[0]: -inc})
                average.append(-inc)
                
            #this compares the absolute value between the prev and nex, if prev is greater than nex,
            #and if nex is a negative, but nex is a bigger number then it is a negative increase
            if prev < nex and int(row[1]) < 0: 
                inc = (abs(prev - nex))
                diff.update({row[0]: inc})
                average.append(inc)

                
        #list updated to represent all of the profit/loss as an int.
        profit.append(int(row[1]))
        #sets the prev value for each for loop.
        prev = int(row[1])
        #adds all of the profit/loss together to create the total.
        total = sum(profit)   

#diff is added and updated during the for loop, adding the date to the increase/decrease value.
#this statement grabs the highest number of profit gain.
maximum = max(diff, key = diff.get)

#this statement grabs the lowest amount of profit loss. 
minimum = min(diff, key = diff.get)

#this statement is used to find the average value of the absolute value difference added into average.
list(map(int, average))
mid = sum(average) / len(average)

#takes the value given from the average statement abov and reduces the decimals and rounds up to the 3rd decimal.
change = (round(mid, 2))


#statement creates a path and allows for the creation of the output.txt,
#all print statements will be written to output.txt
save_path = "Analysis"
name = ("output.txt")
txtpath = os.path.join(save_path, name)
f = open(txtpath, "w")
   
print("", file = f)
print("Financial Analysis", file = f)
print("",file = f)
print("-----------------------------", file = f)
print("", file = f)
print(f"Total Months:", (len(profit)), file = f)
print("", file = f)
print("Total:", ("$" + str(total)), file = f)
print("", file = f)
print(f"Average Change:", "$" + (str(change)), file = f)
print("", file = f)
print(f"The Greatest in Increase:", maximum, "(" + "$" + str(diff[maximum]) + ")", file = f)
print("", file = f)
print(f"The Greatest in Decrease:", minimum, "(" + "$" + str(diff[minimum]) + ")", file = f)
    
f.close()

#this will read the results of the output.txt value in the terminal.
with open(txtpath, "r") as f:
    data = f.read()
    print(data)