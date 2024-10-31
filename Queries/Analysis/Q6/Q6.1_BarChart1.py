import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lettura del file CSV
df = pd.read_csv('./Queries/Analysis/Q6/Q6.csv', sep=',', names=['RepositoryName', 'NumOfContributors', 'Contributor', '%OfContribution'], skiprows=1)

# Assicurarsi che 'NumOfContributors' sia di tipo numerico
df['NumOfContributors'] = pd.to_numeric(df['NumOfContributors'], errors='coerce')

# Rimuovere righe con valori NaN in 'NumOfContributors'
df = df.dropna(subset=['NumOfContributors'])

# Selezionare solo le colonne di interesse e rimuovere duplicati
repositoryContributorsDf = df[['RepositoryName', 'NumOfContributors']].drop_duplicates(subset=['RepositoryName'], keep='first')

# Filtrare repository con numero di contributori maggiore o uguale a 1
repositoryContributorsDf = repositoryContributorsDf[repositoryContributorsDf['NumOfContributors'] >= 1]
# Filtra i repository con 0 contributori
repositories_zero_contributors = df[df['NumOfContributors'] == 0]

# Estrai i primi 19 nomi di repository con 0 contributori
repositories_zero_contributors_names = repositories_zero_contributors['RepositoryName'].head(19)

# Stampa i nomi dei repository
print("Nomi dei primi 19 repository con 0 contributori:")
for repo_name in repositories_zero_contributors_names:
    print(repo_name)


# Definiamo i nuovi bin e le etichette secondo i range specificati
bin_edges = [0, 1, 2, 5, 10, 50, 100, 200, 500, np.inf]
bin_labels = ['[1]', '[2]', '(2,5]', '(5,10]', '(10,50]', '(50,100]', '(100,200]', '(200,500]', '(500+]']

# Crea una distribuzione dei dati usando pd.cut con i nuovi bin definiti
barChartData = pd.cut(repositoryContributorsDf['NumOfContributors'], bins=bin_edges, labels=bin_labels)

# Conta il numero di repository per ciascun intervallo
barChartCounts = barChartData.value_counts().sort_index()

# Creazione del grafico a barre
barChart = barChartCounts.plot.bar(color="green")

plt.xticks(rotation=45)
plt.xlabel('Number of Contributors')
plt.ylabel('Number of Repositories')

# Aggiungi etichette alle barre
barChart.bar_label(barChart.containers[0])

plt.title('Distribution of Repositories by Number of Contributors')
plt.show()
