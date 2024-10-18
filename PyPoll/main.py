# Import libraries
import csv  # To read the CSV files
import os   # To work with file paths

# Set the path 
election_file_path = os.path.join('Resources', 'election_data.csv')

# Initialize the vote counter and dictionary to count votes per candidate
vote_count = 0  
votes_per_candidate = {}  # Store the number of votes each candidate gets

# Open the election data file to read it
with open(election_file_path) as election_file:
    csv_reader = csv.reader(election_file)
    header = next(csv_reader)  # Skip the header row (column names)

    # Loop through the rows in the dataset (each vote)
    for row in csv_reader:
        vote_count += 1  # Increase the total vote count for every row
        candidate_name = row[2]  # The candidate name is in the third column

        # If the candidate is not already in the dictionary, add them
        if candidate_name not in votes_per_candidate:
            votes_per_candidate[candidate_name] = 0
        votes_per_candidate[candidate_name] += 1  # Add a vote to that candidate's total

# Find the candidate with the most votes
winner_name = max(votes_per_candidate, key=votes_per_candidate.get)

# Create the summary of election results
election_summary = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {vote_count}\n"
    f"-------------------------\n"
)

# Loop through the candidates and their vote totals to calculate percentages
for candidate_name, candidate_votes in votes_per_candidate.items():
    vote_percentage = (candidate_votes / vote_count) * 100  # Calculate percentage
    election_summary += f"{candidate_name}: {vote_percentage:.3f}% ({candidate_votes})\n"

# Add the winner to the summary
election_summary += (
    f"-------------------------\n"
    f"Winner: {winner_name}\n"
    f"-------------------------\n"
)

# Print the results 
print(election_summary)

# Set the path to save the results to file
results_save_path = os.path.join('analysis', 'election_results.txt')

# Save the report to file
with open(results_save_path, 'w') as results_file:
    results_file.write(election_summary)  # Write the report to the file
