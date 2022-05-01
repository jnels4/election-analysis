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
#open election results
with open(fileToLoad) as electionData:
    #prepare file to be read
    fileReader = csv.reader(electionData)

    #read the header row
    headers = next(fileReader)
    print(headers)

    #analize our file
    for row in fileReader:
        totalVotes +=1
        #add candidate names to candidate list, avoid duplicates
        candidateName = row[2]
        if candidateName not in candidateList:
            candidateList.append(candidateName)
            #track candidates 
            candidateVotes[candidateName] = 0
        #tally votes in dictionary tied to candidate name
        candidateVotes[candidateName] +=1
    #write to file    
    with open (fileToSave,'w') as txt_file:   
        totalVoteRes = (f'Election Results\n-------------------------\nTotal Votes:{int(totalVotes):,}\n-------------------------\n')
        #print(totalVoteRes, end="")
        txt_file.write(totalVoteRes)
    
    
    #Vote analysis for winner & percentages
    
        for candidateName in candidateList:
            votePercentage = (candidateVotes[candidateName]/totalVotes)*100
            candidateStats = (f'{candidateName}: recieved {votePercentage:.2f}% of the vote. ({candidateVotes[candidateName]})\n')
            txt_file.write(candidateStats)
            if candidateVotes[candidateName] > winningCount and votePercentage > winningPercentage:
                winningCount = candidateVotes[candidateName]
                winningPercentage = votePercentage
                winningCandidate = candidateName
        winSummary =(f'\nThe winner is: {winningCandidate}\nWinning Vote Count: {winningCount}\nWinning Percentage: {winningPercentage:.2f}%')
        txt_file.write(winSummary)
        

