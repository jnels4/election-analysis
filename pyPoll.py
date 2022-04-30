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
        #add candidate names to candidate list
        candidateName = row[2]
        if candidateName not in candidateList:
            candidateList.append(candidateName)
            #track candidates 
            candidateVotes[candidateName] = 0
        candidateVotes[candidateName] +=1
    print (candidateList)
    print (candidateVotes)
    print(totalVotes)
    for candidateName in candidateList:
        votePercentage = (candidateVotes[candidateName]/totalVotes)*100
        print(f'{candidateName}: recieved {votePercentage:.2f}% of the vote. ({candidateVotes[candidateName]})')
        if candidateVotes[candidateName] > winningCount and votePercentage > winningPercentage:
            winningCount = candidateVotes[candidateName]
            winningPercentage = votePercentage
            winningCandidate = candidateName
    print(f'The winner is: {winningCandidate}\nWinning Vote Count: {winningCount}\nWinning Percentage: {winningPercentage:.2f}%')




#Perform Analysis
with open(fileToSave,'w') as txt_file:
    txt_file.write('Hello world 123\n')
    txt_file.write('Counties in the election\n-----------------\nArapahoe\nDenver\nJefferson')

