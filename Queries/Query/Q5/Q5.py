import pandas as pd
import csv
from csv import writer
from datetime import datetime

dfCommits = pd.read_csv('./Queries/Query/Commits_metadata_p1.csv', sep=',', 
            names=['RepositoryName','CommitName','Authors','CommitId','ModifiedFiles','DateTime'])
dfRepository = pd.read_csv('./Queries/Metadata/Repository_metadata.csv', names=['RepositoryName', 'NumberOfStars', 'NumberOfForks', 'NumberOfCommits', 
                       'NumberOfReleases', 'NumberOfContributors', 'NumberOfIssues', 'NumberOfPullRequests'])

for i, row in dfRepository.iterrows():
   
    if(i == 0):
        continue
    else:
        currentRepo = row['RepositoryName']

        repoCommits = dfCommits.query('RepositoryName == @currentRepo')
        
        if(repoCommits.shape[0] > 1):

            firstCommit = repoCommits.iloc[[-1]]
            firstCommitDate = firstCommit['DateTime'].values[0]

            lastCommit = repoCommits.iloc[[0]]
            lastCommitDate = lastCommit['DateTime'].values[0]

            dateFormat = "%Y-%m-%d %H:%M:%S"
            firstCommitDate = datetime.strptime(firstCommitDate, dateFormat)
            lastCommitDate = datetime.strptime(lastCommitDate, dateFormat)
            diffDate = lastCommitDate - firstCommitDate

            frequency = round((diffDate.days+1)/(repoCommits.shape[0]-1),1)

            numOfCommits = repoCommits.shape[0]

            metadata = (currentRepo, numOfCommits, frequency)
            with open('Q5.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(metadata)
        else:
            numOfCommits = repoCommits.shape[0]
            
            metadata = (currentRepo, numOfCommits, "0")
            with open('Q5.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(metadata)   
    
    





