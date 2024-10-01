import pandas as pd
import csv
from csv import writer
from datetime import datetime

dfCommits = pd.read_csv('./Queries/Query/Commits_metadata_p2.csv', sep=',', names=['RepositoryName','CommitName','Authors','CommitId','ModifiedFiles','DateTime'])
dfReleases = pd.read_csv('./Queries/Metadata/Releases_metadata.csv', names=['RepositoryName', 'ReleaseVersion', 'Author', 'ReleaseDateTime', 'LastCommitId'])

for i, row in dfCommits.iterrows():
    
    if(i == 0):
        continue
    else:
        commitDate = row['DateTime']
        currentRepo = row['RepositoryName']
        commitId = row['CommitId']
        print(commitId)
    
        query = " RepositoryName == @currentRepo & ReleaseDateTime == @commitDate "
        releaseOnCommitDate = dfReleases.query(query)

    
        if(len(releaseOnCommitDate) > 0):
            
            metadata = (currentRepo, commitId, commitDate, releaseOnCommitDate['ReleaseVersion'].values[0], releaseOnCommitDate['ReleaseDateTime'].values[0] ,"0", 
                        releaseOnCommitDate['ReleaseVersion'].values[0], releaseOnCommitDate['ReleaseDateTime'].values[0], "0")
            with open('RQ1.1.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(metadata)
        else:
            dateFormat = "%Y-%m-%d %H:%M:%S"
            firstReleaseBeforeCommit = firstReleaseDateBeforeCommit = daysFromFirstReleaseBeforeCommit = "" 
            firstReleaseAfterCommit = firstReleaseDateAfterCommit = daysFromFirstReleaseAfterCommit = ""
            
            repositoryReleases = dfReleases.query(' RepositoryName == @currentRepo ')
            
            if(len(repositoryReleases) == 0):
                continue

            releasesDates = [datetime.strptime(date, dateFormat) for date in repositoryReleases['ReleaseDateTime'].values]
   
            commitDateConverted =  datetime.strptime(commitDate, dateFormat)

            firstReleaseDateAfterCommit =  min(releasesDates, key=lambda x: (x<commitDateConverted, abs(x-commitDateConverted)) ).strftime(dateFormat)     
            firstReleaseDateBeforeCommit =  min(releasesDates, key=lambda x: (x>commitDateConverted, abs(commitDateConverted-x)) ).strftime(dateFormat)   

            if(datetime.strptime(firstReleaseDateAfterCommit, dateFormat)> datetime.strptime(commitDate, dateFormat)):
                firstReleasesAfterCommitWithSameDate = dfReleases.query(' ReleaseDateTime == @firstReleaseDateAfterCommit & RepositoryName == @currentRepo')
                
                firstReleaseAfterCommit = firstReleasesAfterCommitWithSameDate['ReleaseVersion'].values[0].replace(' ','')
                firstReleaseDateAfterCommitDateType = datetime.strptime(firstReleaseDateAfterCommit, dateFormat)

                commitDateConverted =  datetime.strptime(commitDate, dateFormat)
                daysFromFirstReleaseAfterCommit = round(((firstReleaseDateAfterCommitDateType - commitDateConverted).total_seconds()) / 86400,2)
            else:
                firstReleaseAfterCommit = firstReleaseDateAfterCommit = ""
                daysFromFirstReleaseAfterCommit = "0"
            
            if(datetime.strptime(firstReleaseDateBeforeCommit, dateFormat) < datetime.strptime(commitDate, dateFormat)):
                firstReleasesBeforeCommitWithSameDate = dfReleases.query(' ReleaseDateTime == @firstReleaseDateBeforeCommit & RepositoryName == @currentRepo')
                
                firstReleaseBeforeCommit = firstReleasesBeforeCommitWithSameDate['ReleaseVersion'].values[0].replace(' ','')
                firstReleaseDateBeforeCommitDateType = datetime.strptime(firstReleaseDateBeforeCommit, dateFormat)
                
                commitDateConverted =  datetime.strptime(commitDate, dateFormat)
                daysFromFirstReleaseBeforeCommit = round(((commitDateConverted - firstReleaseDateBeforeCommitDateType).total_seconds()) / 86400,2)
            else:
                firstReleaseBeforeCommit = firstReleaseDateBeforeCommit = ""
                daysFromFirstReleaseBeforeCommit = "0"

            metadata = (currentRepo, commitId, commitDate ,firstReleaseBeforeCommit, firstReleaseDateBeforeCommit, daysFromFirstReleaseBeforeCommit, firstReleaseAfterCommit, 
                    firstReleaseDateAfterCommit , daysFromFirstReleaseAfterCommit)
            with open('Q2.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(metadata)  
       
    
    





