# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# Counties and votes in each county
counties=[]
county_votes={}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the county and candidate name from each row.
        county_name=row[1]
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Check if that county is in our list of counties
        # if it is not, add it, and begin tracking
        if county_name not in counties:
            counties.append(county_name)
            county_votes[county_name] = 0
        # add a vote from that county
        county_votes[county_name] += 1

# Save the results to our text file and print to screen
with open(file_to_save, "w") as txt_file:
    # Begin with a header for file and screen
    election_results=(f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        "\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # next is county summary and see who had the highest total
    highCountyVotes=0
    for countyName in counties:
        # Check if current county has highest votes so far
        if county_votes[countyName]>highCountyVotes:
            highCounty=countyName
            highCountyVotes=county_votes[countyName]
        # Determine percent total votes for the county
        percentTotal=float(county_votes[countyName])/float(total_votes)*100
        # Write County Result to screen and file
        countyResult=(f"{countyName}: {percentTotal:.1f}% ({county_votes[countyName]})\n")
        print(countyResult)
        txt_file.write(countyResult)
    # Write County with most votes to screen and file
    highCountySummary=(
    f"-------------------------\n"
    f"Largest County Turnout: {highCounty}\n"
    f"-------------------------\n")
    print(highCountySummary)
    txt_file.write(highCountySummary)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)