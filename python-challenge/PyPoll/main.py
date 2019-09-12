import csv

#total votes, candidate options, candidate votes, winning candidate and their votes
total_votes = 0
candidate_options = []   
candidate_votes = {}
winning_candidate = ""
winner_vote_count = 0

csvpath = "./election_data.csv"

# Convert csv file to a list of dictionaries
with open(csvpath, "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:
            print ('. ', end=""),

            # add to the total votes
            total_votes = total_votes + 1 

            #find the candidate name in each row by looping through the dataset 
            candidate_name = row["Candidate"]

            if candidate_name not in candidate_options:
                #Add candidate to list of candidates
                candidate_options.append(candidate_name)
                #once candidate is added to the list, start tracking their votes
                candidate_votes[candidate_name] = 0
            
            #once new candidate is added, add a vote ot the candidates count
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1 


    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winner_vote_count):
            winner_vote_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)