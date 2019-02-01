#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


import os
import csv

filepath =os.path.join("..","PyBank","budget_data.csv")

#Find the total months and revenues setting a place holder of 0 for both. 
#The += function will replace having to do total=total+1

TotalMonths=0
TotalRevenue=0
with open ("budget_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    csvheader=next(csvreader) #Will skip the header
    for row in csvreader: 
        TotalMonths+=1
        TotalRevenue+=int(row[1])
print(str(TotalMonths))
print(str(TotalRevenue))

#Find the average of the ProfitLosses 
  
   
