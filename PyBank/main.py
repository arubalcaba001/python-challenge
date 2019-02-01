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

Months=[]
Revenue=[]
RevenueChange=[]

with open ("budget_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    csvheader=next(csvreader) #Will skip the header
    for row in csvreader: 
        Months.append(row[0]) #append will hold the values you asked the for to do
        Revenue.append(int(row[1]))

#This will look for the total months and revenue
TotalMonths=len(Months)
TotalRevenue=sum(Revenue)

#Print the results
print(str(TotalMonths))
print(str(TotalRevenue))

#Find the average of the ProfitLosses 
#This for loop will take the Revenue column and subtract from row1-row0, row2-row1 and so forth
#The append will hold the values again

for revrow in range(1,len(Revenue)):
    RevenueChange.append((int(Revenue[revrow])-int(Revenue[revrow-1])))

RevenueChange=sum(RevenueChange)/len(RevenueChange)
print(str(RevenueChange))

#Find the Greatest increase and in revenue the revenue change

GreatestIncrease=max(RevenueChange)
GreatestDecrease=min(RevenueChange)
