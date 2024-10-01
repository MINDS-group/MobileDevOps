import pandas as pd

# Carica i metadati dei repository
dfRepositoryMetadata = pd.read_csv('./Queries/Metadata/Repository_metadata.csv', 
                                   names=['RepositoryName', 'NumberOfStars', 'NumberOfForks', 'NumberOfCommits', 
                                          'NumberOfReleases', 'NumberOfContributors', 'NumberOfIssues', 
                                          'NumberOfPullRequests'], header=0)

# Carica i metadati dei commit dai due file
dfCommitsMetadata_p1 = pd.read_csv('./Queries/Metadata/Commits_metadata_p1.csv', 
                                   names=['RepositoryName', 'CommitName', 'Authors', 'CommitId', 'ModifiedFiles', 'DateTime'], header=0)

dfCommitsMetadata_p2 = pd.read_csv('./Queries/Metadata/Commits_metadata_p2.csv', 
                                   names=['RepositoryName', 'CommitName', 'Authors', 'CommitId', 'ModifiedFiles', 'DateTime'], header=0)

# Combina i due DataFrame dei commit
dfCommitsMetadata = pd.concat([dfCommitsMetadata_p1, dfCommitsMetadata_p2], ignore_index=True)

# Lista di parole chiave per il filtro
keywords = ["Merge", "merge", "merged", "Merged"]

# Funzione per controllare se una stringa contiene una delle parole chiave
def contains_keyword(text):
    if pd.isna(text):
        return False
    return any(keyword in text for keyword in keywords)

# Filtra i commit che contengono le parole chiave
filtered_commits = dfCommitsMetadata[dfCommitsMetadata['CommitName'].apply(contains_keyword)]

# Conta il numero di commit di merge per ciascun repository
merge_counts = filtered_commits.groupby('RepositoryName').size().reset_index(name='NumberOfMerges')

# Unisci i conteggi dei merge ai metadati dei repository
result_df = pd.merge(dfRepositoryMetadata, merge_counts, on='RepositoryName', how='left').fillna(0)

# Salva il risultato in un nuovo file CSV
result_df.to_csv('Repositories_With_Merge_Counts.csv', index=False, encoding='UTF8')

# Mostra il risultato
print(result_df.head())
