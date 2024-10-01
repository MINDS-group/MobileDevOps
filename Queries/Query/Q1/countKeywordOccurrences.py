import pandas as pd
import csv
from csv import writer

dfCommits = pd.read_csv('./Queries/Query/Q1/Q1.csv', sep=',',
            names=['RepositoryName','CommitName','Authors','CommitId','ModifiedFiles','DateTime'])

testKeywords = ["Test","TEST","test","Tests","TESTS","tests","Testing","TESTING","testing"]
deployKeywords = ["Deploy","DEPLOY","deploy","Release","RELEASE","release","Version","VERSION","version","Update","UPDATE","update",
                  "Updating","UPDATING","updating"]

# Change with testKeywords
for keyword in deployKeywords:

    commitNames = dfCommits["CommitName"].values.tolist()

    modifiedFiles = dfCommits["ModifiedFiles"].values.tolist()

    occurrencesInNames = sum(keyword in s for s in commitNames)

    occurrencesInFilePaths = sum(keyword in str(s) for s in modifiedFiles)

    totalOccurrences = occurrencesInNames + occurrencesInFilePaths

    info = [keyword, totalOccurrences]
    
    # Change the name of file csv for the test keywords
    with open('deployKeywordsOccurrences.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(info)