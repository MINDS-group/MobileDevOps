import pandas as pd
import csv
from csv import writer

dfCommits = pd.read_csv('./Queries/Query/Commits_metadata_p2.csv', sep=',',
             names=['RepositoryName','CommitName','Authors','CommitId','ModifiedFiles','CommitDatetime'])
dfRepository = pd.read_csv('./Queries/Metadata/Repository_metadata.csv', names=['RepositoryName', 'NumberOfStars', 'NumberOfForks', 'NumberOfCommits', 
                       'NumberOfReleases', 'NumberOfContributors', 'NumberOfIssues', 'NumberOfPullRequests'])

for i, row in dfRepository.iterrows():
    
    if(i == 0):
        continue
    else:
        currentRepo = row['RepositoryName']
        
        repoCommits = dfCommits.query(' RepositoryName == @currentRepo')
        listOfAuthors = []

        if(repoCommits.shape[0] > 0):
            
            for index, commit in repoCommits.iterrows():
                listOfAuthors.extend(commit["Authors"].split(','))

            authors = set(listOfAuthors)

            numberOfContributors = len(authors)

            for author in authors:

                authorCommits =  repoCommits[repoCommits['Authors'].str.contains(author, na=False, regex=False)]
                numberOfCommits = len(authorCommits)

                authorCommitRate = round(numberOfCommits / len(repoCommits) * 100,2)

                metadata = (currentRepo, numberOfContributors, author, authorCommitRate)
                with open('Q6.csv', 'a', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(metadata)               

        else:
            metadata = (currentRepo, "0", "", "")
            with open('Q6.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(metadata)
        
    
    





