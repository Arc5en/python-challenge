# python-challenge
# For Week 3 Challenge relating to Python
# Disclaimer: Most of the code was inspired from TA Drew's speedrun for this weekly module challenge.
# pybank code:
# Financial Analysis (Expected Results)
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# This code reads a csv file of a budget and returns a few summary statistics including average change and months of most profit.
# This version of the code displayed on the README file includes a few print statements primarly used to test if correct rows are read.


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
    
#     print(reader): test function to ensure reader properly reads csv file
    
    #read header row
    header = next(reader)
    
#     print(f"Header: {header}"): test function to ensure header is correctly read
    
    first_row = next(reader)
    
    total_net = total_net + int(first_row[1])
    prior_net_change = int(first_row[1])
    total_months += 1
    
    for row in reader:
        
#         print(row): test function to ensure rows are read as intended
        
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
            
# print(net_change_list): test function to ensure list is read correctly

# print(max_profit): test function to ensure list is read correctly
# print(min_profit): test function to ensure list is read correctly

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





#pypoll code:
# Expected Output:
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

# As shown in the election results, the function of this code is to read the csv file containing election data 
# to return a few summary statistics and determine the election's winner.
# This version of the code in the README file includes the print functions used to ensure python read the correct rows.

# In[4]:


# Dependencies: modules needed to upload to python to run programs
import csv
import os


# In[10]:


#file to load and output: loading csv file to analyze and outputting results in txt file

file_to_load = os.path.join(".", "Resources", "election_data.csv")

file_to_output = os.path.join(".", "election_analysis.txt")

#Creating variables ahead of time

total_votes = 0

#votes is a dictionary, while options is a list. The former is important to build keys for the latter
candidate_votes = {}
candidate_options = []

#Stats for Winning Candidate
winning_candidate = " "
winning_count = 0


#User csv.reader to read the csv file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    #Read header row
    header = next(reader)
#     print(header): test function to ensure correct row is read as header
    
    #Read each row
    for row in reader:
        
        #Accumulate sum of total votes
        total_votes = total_votes + 1
#         print(row): test function to ensure rows are read

        #Collect candidate names from each row
        candidate_name = row[2]
        
        #Record unique candidate names in our candidate_options list and attach as key to votes dictionary
        
        if candidate_name not in candidate_options:
            
            #Add to options list
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1
    
#     print(candidate_votes): *test function to ensure variable above is read*
#     print(candidate_options): * * (* * indicates identical statement to one above this line ^)
        
#Start creating text file with poll analysis
with open(file_to_output, "w") as txt_file:
    
    #Record data for Total Votes
    election_results = (
        f"Election Results\n"
        f"------------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------------------------\n"

    )


    print(election_results)

    txt_file.write(election_results)

    #Record data for Candidate Votes
    for candidate in candidate_votes:

        votes = candidate_votes[candidate]
        vote_percentage = float(votes/total_votes) * 100

        #Store data for Winning Candidate for future reference
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
        
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    #     print(votes): * *
    #     print(vote_percentage): * *
        print(voter_output)
        
        txt_file.write(voter_output)
    
    #Record data for winning candidate
    winning_candidate_summary = (
        f"------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"------------------------------------------\n"
    )

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
