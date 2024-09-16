# Import library and modules
import pandas as pd
from pathlib import Path

# Read a .csv file 'Commits_metadata_p2.csv'
dataframe = pd.read_csv('./AutomaticAnalysis/Commits_metadata_p2.csv', names = ['RepositoryName', 'CommitName', 'Authors', 'CommitId', 'ModifiedFiles', 'DateTime'], sep=',')

print(dataframe)

# Delete firsts columns
dataframe.drop(['RepositoryName', 'Authors', 'CommitId', 'ModifiedFiles', 'DateTime'], axis=1, inplace=True)
print(dataframe)

# Checking if there are NaN values.
dataframe.isnull().any()

# Check the NaN values in the column 'CommitName'
dataframe[dataframe['CommitName'].isnull()]

# Delete NaN values
dataframe.dropna(inplace=True)

# Check if the NaN values are deleted
dataframe.isnull().any()

print(dataframe.dtypes)

# Saving the cleaned dataframe, so we can easly use it.
filepath = Path('./AutomaticAnalysis/Dataframe2.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
dataframe.to_csv(filepath, sep=',')