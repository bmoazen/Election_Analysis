# Election_Analysis
# Overview of Election Audit
The Colorado Election Board has tasked us with certifying the results of an election for a US congressional seat in Colorado. Our deliverables are: the total number of votes cast, total votes by county, vote totals and percentages by candidate, as well as certifying the overall winner. To accomplish this, we used Python version 3.6.1 with Visual Studio COde 1.38.1.

## Resources
Data Source: election_results.csv
Software: Python 3.6.1, Visual Studio Code 1.38.1

## Election-Audit Results
With 73.8% of the 369,711 total votes cast, Diana DeGette is the winner of this election.  
Diana DeGette: 272,892 votes (73.8%)<br />
Charles Casper Stockham: 85,213 votes (23.0%)<br />
Raymon Anthony Doane: 11,606 (3.1%)<br />
<br />
The breakdown of votes cast by county are as follows:<br />
Denver County: 305,055 votes (82.8%)<br />
Jefferson County 38,855 (10.5%)<br />
Arapahoe County: 24801 (6.7%)<br />
Total Votes: 369,711<br />

# Election-Audit Summary
One piece of information that may be very helpful in an election audit would be the percentage of votes for each candidate in each county. The existing code Pypoll_Challenge code<br /> (https://github.com/bmoazen/Election_Analysis/blob/main/Pypoll_Challenge.py),br /n>
could easily be modified to calculate this. The dictionary "county_votes" could be modified to include a subdictionary that counts the number of votes by candidate. Each value in "county_votes" would have two keys. For example, line 54 in Pypoll_Challenge:<br />
          county_votes[county_name] += 1 <br />
would then be modified to:<br />
          county_votes[county_name,candidate_name] += 1 <br />
Then we would have the vote totals for each county broken down by candidate. This could be extremely useful for later calculations, for instance, to see what counties a candidate did well in as opposed to others.<br />
<br />
If this script were to be used for a national election, there would be a additional information (state of the voter) that would be included.  In this case, we would make "total votes" a dictionary so that we could track votes by state and county.
