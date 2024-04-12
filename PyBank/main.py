#Imports I might need
import os
import csv
import statistics

#Empty lists for the data to go
months = []
PL = []
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
        PL = [int(i) for i in PL] #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
#Find the total number of months
    print(len(months))
# Net Profits and Loss
    net = sum(PL)
    print(str(net))
#Avg Change
    change = [PL[i] - PL[i + 1] for i in range(len(PL) - 1)] #https://www.reddit.com/r/learnpython/comments/tg3xdi/i_have_a_list_of_numbers_how_do_i_subtract_the/
    avgchange = statistics.mean(change) #https://www.w3schools.com/python/ref_stat_mean.asp#:~:text=mean()%20method%20calculates%20the,how%20many%20values%20there%20are.
    print(str(avgchange)) #should this be negative???
   
    
