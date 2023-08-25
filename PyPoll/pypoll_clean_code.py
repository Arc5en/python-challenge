#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# As shown in the election results, the function of this code is to read the csv file containing election data 
# to return a few summary statistics and determine the election's winner.
# This version of the code was cleaned to remove any function/comment related to debugging.


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
    
    #Read each row
    for row in reader:
        
        #Accumulate sum of total votes
        total_votes = total_votes + 1

        #Collect candidate names from each row
        candidate_name = row[2]
        
        #Record unique candidate names in our candidate_options list and attach as key to votes dictionary
        
        if candidate_name not in candidate_options:
            
            #Add to options list
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1
        
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


# In[ ]:




