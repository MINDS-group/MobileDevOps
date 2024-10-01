import pandas as pd
import csv
from csv import writer

dfCommits = pd.read_csv('.Queries/Query/Commits_metadata_p2.csv', sep=',', 
            names=['RepositoryName','CommitName','Authors','CommitId','ModifiedFiles','DateTime'])

for i, row in dfCommits.iterrows():
    
    if(i == 0):
        continue
    else:

        modifiedFiles = str(row['ModifiedFiles'])
        
        if(modifiedFiles != 'nan'):
            modifiedFiles = modifiedFiles.split(',')
        else: 
            modifiedFiles = []

        numberOfFiles = len(modifiedFiles)    

        metadata = (row['RepositoryName'], row['CommitId'], numberOfFiles)
        with open('Q4.csv', 'a', encoding='UTF8', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(metadata)
    
    
    





