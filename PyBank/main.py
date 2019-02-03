#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results

import os
import csv

filepath =os.path.join("..","PyBank","budget_data.csv")

#Set all of the holders and read the csv files

Months=[]
Revenue=[]
RevenueChange=[]
RevenueChangeDate=[]

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
print("Total Months: "+ str(TotalMonths))
print("Total Revenue: "+"$"+str(TotalRevenue))

#Find the average of the ProfitLosses 
#This for loop will take the Revenue column and subtract from row1-row0, row2-row1 and so forth.  Use the range functions
#The append will hold the values again

for revrow in range(1,len(Revenue)):
    #Hold the revenue change and date to start with the revenue before the first role
    RevenueChange.append((int(Revenue[revrow])-int(Revenue[revrow-1]))) #Hold the revenue change
    RevenueChangeDate.append(str(Months[revrow]))
    #Find the average revenue change
    AverageRevenueChange=sum(RevenueChange)/len(RevenueChange)
    #Find the max and min of revenue change
    MaxRevenueChange=max(RevenueChange)
    MinRevenueChange=min(RevenueChange)
    #Find the largest Increase by using index to find the row of maximum and minimu revenue change and that will find the month
    MaxRevenueChangeDate=RevenueChangeDate[RevenueChange.index(max(RevenueChange))]
    MinRevenueChangeDate=RevenueChangeDate[RevenueChange.index(min(RevenueChange))]

print("Financial Analysis")
print("=================================")
print("Average Revenue Change: "+"$"+str(AverageRevenueChange))
print("Greatest Increase in Profits: "+str(MaxRevenueChangeDate)+ " ($" + str(MaxRevenueChange) +")")
print("Greatest Decrease in Profits: "+str(MinRevenueChangeDate)+ " ($" + str(MinRevenueChange) +")")

#Output to a text file
NewFile = open("PyBankOutput.txt","w")
NewFile.write("Financial Analysis"+ "\n")
NewFile.write("================================="+"\n")
NewFile.write("Total Months: "+ str(TotalMonths) + "\n")
NewFile.write("Total Revenue: "+"$"+str(TotalRevenue)+"\n")
NewFile.write("Average Revenue Change: "+"$"+str(AverageRevenueChange)+"\n")
NewFile.write("Greatest Increase in Profits: "+str(MaxRevenueChangeDate)+ " ($" + str(MaxRevenueChange) +")"+"\n")
NewFile.write("Greatest Decrease in Profits: "+str(MinRevenueChangeDate)+ " ($" + str(MinRevenueChange) +")"+ "\n")
NewFile.close()