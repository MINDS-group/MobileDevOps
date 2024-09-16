import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lettura del file CSV
df = pd.read_csv('./Queries/Analysis/Q6/Q6.csv', sep=',', names=['RepositoryName', 'NumOfContributors', 'Contributor', '%OfContribution'], skiprows=1)

# Assicurarsi che 'NumOfContributors' sia di tipo numerico
df['NumOfContributors'] = pd.to_numeric(df['NumOfContributors'], errors='coerce')

# Rimuovere righe con valori NaN in 'NumOfContributors'
df = df.dropna(subset=['NumOfContributors'])

# Selezionare solo le colonne di interesse
repositoryContributorsDf = df[['RepositoryName', 'NumOfContributors']]

# Rimuovere duplicati
repositoryContributorsDf = repositoryContributorsDf.drop_duplicates(subset=['RepositoryName'], keep='first')

# Filtrare repository con 0 contributori
repos_with_zero_contributors = repositoryContributorsDf[repositoryContributorsDf['NumOfContributors'] == 0]

# Controlla quanti repository hanno 0 contributori
print(f"Numero di repository con 0 contributori: {len(repos_with_zero_contributors)}")

# Mostra i repository con 0 contributori
print("\nRepository con 0 contributori:")
print(repos_with_zero_contributors)

# Definiamo i bin e le etichette
bin_edges = [-0.5, 0.5, 2.5, 5.5, 9.5, np.inf]
bin_labels = ['[0]', '[1,2]', '[3,5]', '[6,9]', '[10+]']

# Crea una distribuzione dei dati usando pd.cut con i bin definiti
barChartData = pd.cut(repositoryContributorsDf['NumOfContributors'], bins=bin_edges, labels=bin_labels)

# Conta il numero di repository per ciascun intervallo
barChartCounts = barChartData.value_counts().sort_index()

# Verifica se ci sono repository fuori intervallo che dovrebbero essere inclusi
num_out_of_bounds = len(repositoryContributorsDf) - len(barChartData.dropna())
if num_out_of_bounds > 0:
    # Aggiungi i repository fuori intervallo a '[10+]' se non esistono ancora
    if '[10+]' in barChartCounts.index:
        barChartCounts['[10+]'] += num_out_of_bounds
    else:
        barChartCounts['[10+]'] = num_out_of_bounds

# Creazione del grafico a barre
barChart = barChartCounts.plot.bar(color="green")

plt.xticks(rotation=0)
plt.xlabel('Number of Contributors')
plt.ylabel('Number of Repositories')

# Aggiungi etichette alle barre
barChart.bar_label(barChart.containers[0])

plt.show()
