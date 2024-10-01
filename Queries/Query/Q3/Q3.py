import pandas as pd
import csv
from csv import writer
from datetime import datetime

dfRepository = pd.read_csv('./Queries/Metadata/Repository_metadata.csv', names=['RepositoryName', 'NumberOfStars', 'NumberOfForks', 'NumberOfCommits', 
                       'NumberOfReleases', 'NumberOfContributors', 'NumberOfIssues', 'NumberOfPullRequests'])
dfReleases = pd.read_csv('./Queries/Metadata/Releases_metadata.csv', names=['RepositoryName', 'ReleaseVersion', 'Author', 'ReleaseDateTime', 'LastCommitId'])

for i, row in dfRepository.iterrows():
    
    if( i == 0):
        continue

    currentRepo = row['RepositoryName']

    result = dfReleases.query('RepositoryName == @currentRepo')

    if(result.shape[0] > 1):

        firstRelease = result.iloc[[-1]]
        firstReleaseDate = firstRelease['ReleaseDateTime'].values[0]

        lastRelease = result.iloc[[0]]
        lastReleaseDate = lastRelease['ReleaseDateTime'].values[0]

        dateFormat = "%Y-%m-%d %H:%M:%S"
        firstReleaseDate = datetime.strptime(firstReleaseDate, dateFormat)
        lastReleaseDate = datetime.strptime(lastReleaseDate, dateFormat)
        diffDate = lastReleaseDate - firstReleaseDate

        frequenza = round((diffDate.days+1)/(result.shape[0]-1),1)

        numOfReleases = result.shape[0]

        metadata = (currentRepo, numOfReleases, frequenza)
        with open('Q3.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(metadata)
    else:

        numOfReleases = result.shape[0]

        metadata = (currentRepo, numOfReleases, "0")
        with open('Q3.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(metadata)
        
    
    





