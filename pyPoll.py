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
#open election results
with open(fileToLoad) as electionData:
    fileReader = csv.reader(electionData)
    headers = next(fileReader)
    print(headers)

#Perform Analysis
with open(fileToSave,'w') as txt_file:
    txt_file.write('Hello world 123\n')
    txt_file.write('Counties in the election\n-----------------\nArapahoe\nDenver\nJefferson')

