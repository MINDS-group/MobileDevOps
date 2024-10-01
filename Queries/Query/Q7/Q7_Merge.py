import pandas as pd
import csv

dfRepositoryMetadata = pd.read_csv('./Queries/Query/Commits_metadata_p1.csv', sep=',',
                                   names=['RepositoryName', 'CommitName', 'Authors', 'CommitId', 'ModifiedFiles', 'DateTime'])

mergeKeywords = ["Merge", "merge", "merged", "Merged"]

# Change with testKeywords
for keyword in mergeKeywords:

    commitNames = dfRepositoryMetadata["CommitName"].fillna("").astype(str).values.tolist()

    modifiedFiles = dfRepositoryMetadata["ModifiedFiles"].fillna("").astype(str).values.tolist()

    occurrencesInNames = sum(keyword in str(s) for s in commitNames)

    occurrencesInFilePaths = sum(keyword in str(s) for s in modifiedFiles)

    totalOccurrences = occurrencesInNames + occurrencesInFilePaths

    info = [keyword, totalOccurrences]

    # Change the name of file csv for the test keywords
    with open('./Queries/Query/Q7/Q7_Keywords_Merge.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(info)
        