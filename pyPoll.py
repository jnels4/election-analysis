#Need to retrieve
#total votes cast
#list of candidates
#total votes per candidate
#percentage of votes per candidate
#determine who won based on percentage
import os
import csv
#save path
fileToLoad = os.path.join('Resources','election_results.csv')
fileToSave = os.path.join('analysis','election_analysis.txt')

#initialize total votes
totalVotes = float(0) 
#initialize candidate options
candidateList = []
#dictionary to hold election data
candidateVotes = {}
#create winning condition
winningCandidate = ''
winningCount = 0
winningPercentage = 0

#determine county results
countyVotes = {}
countyList = []
countyVoteNum = 0
largestCountyVotes = 0

#open election results
with open(fileToLoad) as electionData:
    #prepare file to be read
    fileReader = csv.reader(electionData)

    #read the header row
    headers = next(fileReader)
    #print(headers)

    #analize our file
    for row in fileReader:
        totalVotes +=1
        #add candidate names to candidate list, avoid duplicates
        candidateName = row[2]
        countyName = row[1]
        if countyName not in countyList:
            #track counties
            countyList.append(countyName)
            #innitialize votes to 0 for any county being added to dictioary
            countyVotes[countyName]=0
        if candidateName not in candidateList:
            candidateList.append(candidateName)
            #track candidates 
            candidateVotes[candidateName] = 0
        #tally votes in dictionary tied to candidate name
        candidateVotes[candidateName] +=1
        countyVotes[countyName] +=1
    
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
        


    #Vote analysis for winner & percentages
    
        for candidateName in candidateList:
            votePercentage = (candidateVotes[candidateName]/totalVotes)*100
            candidateStats = (f'{candidateName}: recieved {votePercentage:.2f}% of the vote. ({candidateVotes[candidateName]:,})\n')
            txt_file.write(candidateStats)
            if candidateVotes[candidateName] > winningCount and votePercentage > winningPercentage:
                winningCount = candidateVotes[candidateName]
                winningPercentage = votePercentage
                winningCandidate = candidateName
            print (candidateStats)
        winSummary =(f'\nThe winner is: {winningCandidate}\nWinning Vote Count: {winningCount:,}\nWinning Percentage: {winningPercentage:.2f}%')
        print(winSummary)
        txt_file.write(winSummary)
        

