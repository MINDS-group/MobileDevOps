import pandas as pd
import csv
from csv import writer

dfRepositoryMetadata = pd.read_csv('./Queries/Metadata/Repository_metadata.csv', 
                       names=['RepositoryName', 'NumberOfStars', 'NumberOfForks', 'NumberOfCommits', 
                       'NumberOfReleases', 'NumberOfContributors', 'NumberOfIssues', 
                       'NumberOfPullRequests'])

for i, row in dfRepositoryMetadata.iterrows():
    
    if(i == 0):
        continue
    else:
        currentRepo = row['RepositoryName']
        NumberOfPullRequests = row['NumberOfPullRequests']
        NumberOfForks = row['NumberOfForks']

        metadata = (currentRepo, NumberOfPullRequests, NumberOfForks)
        with open('Q7.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(metadata)
   
    
    





