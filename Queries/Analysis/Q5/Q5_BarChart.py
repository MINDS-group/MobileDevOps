import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Leggi il file CSV originale
csvFile = pd.read_csv('./Queries/Analysis/Q5/Q5.csv', sep=',', names=['RepositoryName', 'NumOfCommits', 'CommitFrequency (days)'], skiprows=1)

# Assicurati che 'CommitFrequency (days)' sia numerico
csvFile['CommitFrequency (days)'] = pd.to_numeric(csvFile['CommitFrequency (days)'], errors='coerce')

# Rimuovi duplicati in base al nome del repository
csvFile = csvFile.drop_duplicates(subset=['RepositoryName'])

# Verifica il numero totale di repository nel dataset originale
total_repositories_original = csvFile['RepositoryName'].nunique()
print(f"Totale repository nel dataset originale: {total_repositories_original}")

# Controllare i valori minimi e massimi nella colonna "CommitFrequency (days)"
min_value = csvFile['CommitFrequency (days)'].min()
max_value = csvFile['CommitFrequency (days)'].max()
print(f"Valore minimo in 'CommitFrequency (days)': {min_value}")
print(f"Valore massimo in 'CommitFrequency (days)': {max_value}")

# Includere tutti i repository nei bin, compresi quelli con frequenze di commit pari a 0 o negativi
bins = [-np.inf, 0, 2, 5, 9, np.inf]
labels = ['[0]', '[1,2]', '[3,5]', '[6,9]', '[10+]']
barChartData = pd.cut(csvFile['CommitFrequency (days)'], bins=bins, labels=labels)

# Conta il numero di repository per ciascun intervallo
barChartCounts = barChartData.value_counts().sort_index()

# Verifica il numero totale di repository inclusi
total_repositories_included = barChartCounts.sum()
print(f"Totale repository inclusi nell'analisi: {total_repositories_included}")

# Verifica se ci sono duplicati che potrebbero causare il problema
duplicate_repositories = csvFile[csvFile.duplicated(subset=['RepositoryName'], keep=False)]
print(f"Repository duplicati trovati: {len(duplicate_repositories)}")

# Visualizza il numero totale di repository per ciascun intervallo
print("Conteggio dei repository per intervallo:")
print(barChartCounts)

# Crea un grafico a barre per visualizzare la distribuzione
barChart = barChartCounts.plot.bar(color="green")

# Aggiungi etichette al grafico
plt.xticks(rotation=0)
plt.xlabel('Commit Frequency (Days)') 
plt.ylabel('Number Of Repositories')

barChart.bar_label(barChart.containers[0])

# Mostra il grafico
plt.show()
