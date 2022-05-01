# election-analysis

## Project Overview

A an Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

**Tasks**
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate receieved.
4. Calculate the percentage of votes each candidate won.
5. Determin the final winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code (most recent release)


## Summary
The analysis of the election results showed thatt:
- There were 369,711 votes cast in the election.
- There were 3 candidates:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane


The results were:

   - Charles Casper Stockham: recieved 23.05% of the vote. (85213)
    
   - Diana DeGette: recieved 73.81% of the vote. (272892)
    
   - Raymon Anthony Doane: recieved 3.14% of the vote. (11606)
    
The winner of the election was determined to be: **Diana DeGette**

 - Winning Vote Count: 272892

 - Winning Percentage: 73.81%

## Additional Analysis

The election employee wanted more information on a per-county basis as to how many votes each county had and the percentage of votes each county had of the total popular vote.  Additionally, they wanted to know the county with the most overall votes.

**Tasks**
1. Create a list of the counties for this election.
2. Determine the number of votes for each county.
3. Determine the percentage of votes from the total popular vote.
4. Determine the county with the most total votes.

## Summary

Analysis of the results showed that there were 3 different counties in the election data.  This data was too large to parse by hand, so we created a script that would add each unique county name to a list of counties. 

    #track and add unique counties to the list of counties
        if countyName not in countyList:
            #track counties
            countyList.append(countyName)
            #innitialize votes to 0 for any county being added to dictioary
            countyVotes[countyName]=0


The counties in the list were:

- Denver
- Jefferson
- Arapahoe

The results showed that:

   - Denver had a total of: 82.78% of the total votes casted. (306,055) ** **Highest Turnout** **
    
   - Jefferson had a total of: 10.51% of the total votes casted. (38,855)
    
   - Arapahoe had a total of: 6.71 of the total votes casted. (24,801)

## Moving Forward


The scripts used to determine the winning candidate can be used and adopted easily for any election.  We can adapt this script to a larger set of data by instead writing the new analysis to a CSV (if the data spans hundreds or thousands of counties).  We can additionally reformat any piece of this code quite easily to meet the needs of any client.

For an election comission, we can very easily analyze the total percentage of citizens that voted per county.  The commission could then focus on increasing voter turn out in any county/town/village/etc. that had a low percentage of voter turn out.  Our results could help inform a statewide voter turn out campaign to increase particpation in the election process.

Addtionally, we can very easily add analysis on a per-county basis.  This would be particularly useful information for a candidate.  If a candidate wanted to focus in directly ony any county (or combination of counties), we could easily do that programatically, and produce any type of analysis they needed.  Doing this type of analysis would allow a candidate to narrow in and focus on a county or group of counties that they wanted to direct their campaign efforts to. 
    
    
    
   
