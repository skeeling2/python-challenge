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
        PL = [int(i) for i in PL] 
#"Python Converting All Strings In List To Integers." Geeks for Geeks,
#https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/. Accessed 12 April 2024
  
# Net Profits and Loss
    net = sum(PL)

#Avg Change - Subtract the rows from the one before it and then take an average of those values
    change = [PL[i+1] - PL[i] for i in range(len(PL) - 1)] 
#[Shiba_Take] "I have a list of numbers. How do I subtract the current number with the next number?" Reddit,   
#https://www.reddit.com/r/learnpython/comments/tg3xdi/i_have_a_list_of_numbers_how_do_i_subtract_the/. Accessed 12 April 2024.

    avgchange = round(statistics.mean(change),2) 
#"Python statistics.mean() Method." W3 Schools,    
#https://www.w3schools.com/python/ref_stat_mean.asp#:~:text=mean()%20method%20calculates%20the,how%20many%20values%20there%20are. Accessed 12 April 2024.

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

export_file = os.path.join("..","PyBank","Analysis","PyBankResults.txt")
with open(export_file, "w") as text:
    text.write("Financial Analysis\n\n")
    text.write("-----------------------------\n\n")
#Find the total number of months
    text.write("Total Months: " + str(len(months)) +"\n\n")
    text.write("Total: $" + (str(net)) + "\n\n")
    text.write("Average Change: $" +str(avgchange) +"\n\n")
#Use the index of the change value to find the corresponding month in the month list. Add because the rows will be off since the first value isn't getting subtracted.
    text.write("Greatest Increase in Profits: " + months[maxinc_index+1] + " " + "($" + str(maxinc) + ")\n\n")
    text.write("Greatest Decrease in Profits: " + months[maxdec_index+1] + " " + "($" + str(maxdec) + ")\n\n")
#Singh, Sharika. "How to write multiple lines in text file using Python?" Tutorialspoint,
#https://www.tutorialspoint.com/How-to-write-multiple-lines-in-text-file-using-Python. Accessed 14 April 2024.
