#!/usr/bin/env python
# coding: utf-8

# In[2]:

# This code reads a csv file of a budget and returns a few summary statistics including average change and months of most profit.
# This version of code is cleaner by removing any statements utilized for debugging.


# Dependencies: modules I need to upload to python to run programs
import csv
import os


#file to load and output: loading csv file to analyze and outputting results in txt file

file_to_load = os.path.join(".", "Resources", "budget_data.csv")

file_to_output = os.path.join(".", "budget_analysis.txt")

#Setting a few variables and lists
total_months = 0
total_net = 0


net_change_list = []
month_of_change = []

max_profit = ["", 0]
#Any arbitrarily large number is suitable provided that it exceeds the largest data point in a given set
min_profit = ["", 9999999999999]

#Read csv file and convert into a list printed in Python
with open(file_to_load) as budget_data:
    
    reader = csv.reader(budget_data)
    
    #read header row
    header = next(reader)
    
    first_row = next(reader)
    
    total_net = total_net + int(first_row[1])
    prior_net_change = int(first_row[1])
    total_months += 1
    
    for row in reader:
        
        #track total months
        total_months += 1
        
        #track total net
        total_net = total_net + int(row[1])
        
        #track net change
        net_change = int(row[1]) - prior_net_change
        prior_net_change = int(row[1])
        net_change_list.append(net_change)
        
        #Finding the greatest increase
        if(net_change > max_profit[1]):
            max_profit[0] = row[0]
            max_profit[1] = net_change
            
        #Finding the greatest decrease
        if(net_change < min_profit[1]):
            min_profit[0] = row[0]
            min_profit[1] = net_change

average_change = sum(net_change_list)/len(net_change_list)


output = (
    f"Financial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profits/Losses: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_profit[0]} (${max_profit[1]})\n"
    f"Greatest Decrease in Profits: {min_profit[0]} (${min_profit[1]})\n"
)

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


# In[ ]:




