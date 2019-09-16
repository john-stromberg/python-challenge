#import dependencies
import os
import csv

#declare csv file path
data = os.path.join("..", "Resources", "budget_data.csv")

#read csv file 
with open(data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

#determine total months and net amount of profit/loss
    months = []
    profit_loss = []

    for rows in csv_reader:
        months.append(rows[0])
        profit_loss.append(int(rows[1]))
    
    total_months = len(months)
    total_pl = sum(profit_loss)

#determine change in profit/losses to determine average, min, max changes
    pl_change = []
    
    for x in range(1, len(profit_loss)):
        pl_change.append(int(profit_loss[x]-int(profit_loss[x-1])))

    pl_average = sum(pl_change) / len(pl_change)

    greatest_increase = max(pl_change)
    greatest_decrease = min(pl_change)

#print results 
    print("Financial Analysis")
    print("_____________________________")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_pl))
    print("Average Change: " + "$" + str(pl_average))
    print("Greatest Increase In Profit: " + "$" + str(greatest_increase))
    print("Greatest Decrease In Profit: " + "$" + str(greatest_decrease))

#export results to text file
file = open("analysis.txt", "w")
file.write("Financial Analysis" + "\n")
file.write("_____________________________" + "\n")
file.write("Total Months: " + str(total_months) + "\n")
file.write("Total: " + "$" + str(total_pl) + "\n")
file.write("Average Change: " + "$" + str(pl_average) + "\n")
file.write("Greatest Increase In Profit: " + "$" + str(greatest_increase) + "\n")
file.write("Greatest Decrease In Profit: " + "$" + str(greatest_decrease) + "\n")
