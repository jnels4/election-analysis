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


The results per candidate were:

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

Once we determined each unique county, we needed to tabulate their votes and the percentage of the total vote.  You can see from the code below, we did this at the same time for the candidates and thte counties. 

     #tally votes in dictionary tied to candidate name
        candidateVotes[candidateName] +=1
        countyVotes[countyName] +=1
        
We had the totals per county (and candidate), and we needed to determine ther percentages and the county with the highest turnout. To do that, we had to use the total votes per county and divide that by the total number of votes.  To do that, we used a for loop to iterate through each county in our county list, and then an if statement to determine if thte total number of votes was higher than the previous value of "largestCountyVotes" which was our place holder for the county with the largest vote turnout. If the current value of votes was larger than "largestCountyVotes" that became our largest county.  Once all of the counties had run through our algorithm, the largest turnout county was identified and reported.  We used a basic text file to store the output, as well as console reporting for ourselves while we were working and debugging our code.  The same(ish) formula was used to determine the winning candidate(shown above).  

    #write to file    
    with open (fileToSave,'w') as txt_file:   
        totalVoteRes = (f'Election Results\n-------------------------\nTotal Votes:{int(totalVotes):,}\n-------------------------\nCounty Votes:\n')
        #print(totalVoteRes, end="")
        txt_file.write(totalVoteRes)
        print(totalVoteRes)
    #Vote analysis for county turnour
        for countyName in countyList:
            countyVotePercentage = (countyVotes[countyName]/totalVotes)*100
            countyStats = (f'{countyName}: {countyVotePercentage:.2f} ({countyVotes[countyName]:,})\n')
            print (countyStats)
            txt_file.write(countyStats)
            if (countyVotes[countyName] > largestCountyVotes):
                largestCountyVotes = countyVotes[countyName]
                largestCounty = countyName
                voterTurnout = (f'\n-------------------------\nThe largest county turnout was: {largestCounty} ({largestCountyVotes:,})\n-------------------------\n')
        txt_file.write(voterTurnout)
        print(voterTurnout)

The results showed that:

   - Denver had a total of: 82.78% of the total votes casted. (306,055) ** **Highest Turnout** **
    
   - Jefferson had a total of: 10.51% of the total votes casted. (38,855)
    
   - Arapahoe had a total of: 6.71 of the total votes casted. (24,801)

## Moving Forward


The scripts used to determine the winning candidate can be used and adopted easily for any election.  We can adapt this script to a larger set of data by instead writing the new analysis to a CSV (if the data spans hundreds or thousands of counties).  We can additionally reformat any piece of this code quite easily to meet the needs of any client.

For an election comission, we can very easily analyze the total percentage of citizens that voted per county.  The commission could then focus on increasing voter turn out in any county/town/village/etc. that had a low percentage of voter turn out.  Our results could help inform a statewide voter turn out campaign to increase particpation in the election process.

Addtionally, we can very easily add analysis on a per-county basis.  This would be particularly useful information for a candidate.  If a candidate wanted to focus in directly ony any county (or combination of counties), we could easily do that programatically, and produce any type of analysis they needed.  Doing this type of analysis would allow a candidate to narrow in and focus on a county or group of counties that they wanted to direct their campaign efforts to. 
    
    
    
   
