#Imports I might need
import os
import csv
import statistics

#Empty lists for the data to go
months = []
PL = []
    #Need to add this list when you get to the average change
change = []

#Find the csv
budgetcsv = os.path.join('..','PyBank','Resources','budget_data.csv')

#Read a csv
with open(budgetcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

#Skip the headers
    csv_header = next(csvreader)

#Put the data into the lists
    for row in csvreader:
        months.append(row[0])
        PL.append(row[1])
        #Make sure the PL values are integers so you can do math
        PL = [int(i) for i in PL] #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
  
# Net Profits and Loss
    net = sum(PL)

#Avg Change - Subtract the rows from the one before it and then take an average of those values
    change = [PL[i+1] - PL[i] for i in range(len(PL) - 1)] #https://www.reddit.com/r/learnpython/comments/tg3xdi/i_have_a_list_of_numbers_how_do_i_subtract_the/
    avgchange = round(statistics.mean(change),2) #https://www.w3schools.com/python/ref_stat_mean.asp#:~:text=mean()%20method%20calculates%20the,how%20many%20values%20there%20are.

#Greatest increase over time period
maxinc = max(change)
    #Get the index of the max change number to print the corresponding month at the end
maxinc_index = change.index(maxinc)

#Greatest decrease
maxdec = min(change)
    #Get the index of the min increase (max decrease) to print the corresponding month at the end.
maxdec_index = change.index(maxdec)


# Print OutPut
print()
print("Financial Analysis")
print()
print()
print("-----------------------------")
print()
print()
#Find the total number of months
print("Total Months: " + str(len(months)))
print()
print()
print("Total: $" + (str(net)))
print()
print()
print("Average Change: $" +str(avgchange))
print()
print()
#Use the index of the change value to find the corresponding month in the month list. Add because the rows will be off since the first value isn't getting subtracted.
print("Greatest Increase in Profits: " + months[maxinc_index+1] + " " + "($" + str(maxinc) + ")")
print()
print()
print("Greatest Decrease in Profits: " + months[maxdec_index+1] + " " + "($" + str(maxdec) + ")")

export_file = open("PyBankResults.txt", "w")
print("Financial Analysis",file = export_file)
print("-----------------------------",file = export_file)
#Find the total number of months
print("Total Months: " + str(len(months)),file = export_file)
print("Total: $" + (str(net)),file = export_file)
print("Average Change: $" +str(avgchange),file = export_file)
#Use the index of the change value to find the corresponding month in the month list. Add because the rows will be off since the first value isn't getting subtracted.
print("Greatest Increase in Profits: " + months[maxinc_index+1] + " " + "($" + str(maxinc) + ")",file = export_file)
print("Greatest Decrease in Profits: " + months[maxdec_index+1] + " " + "($" + str(maxdec) + ")",file = export_file)
export_file.close()
