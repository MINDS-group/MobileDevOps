import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leggi il file CSV
dfRepositoryMetadata = pd.read_csv('./Queries/Analysis/Q7/Repositories_With_Merge_Counts.csv', sep=',', header=0)

# Verifica le colonne e i tipi di dati
print("Colonne nel DataFrame:", dfRepositoryMetadata.columns)
print("Tipi di dati nel DataFrame:", dfRepositoryMetadata.dtypes)

# Converti la colonna 'NumberOfMerges' in numerica, forzando i valori non numerici a NaN
dfRepositoryMetadata['NumberOfMerges'] = pd.to_numeric(dfRepositoryMetadata['NumberOfMerges'], errors='coerce').fillna(0)

# Verifica il numero totale di repository nel dataset
total_repositories_original = len(dfRepositoryMetadata)
print(f"Totale repository nel dataset originale: {total_repositories_original}")

# Verifica la gamma di valori
min_value = dfRepositoryMetadata['NumberOfMerges'].min()
max_value = dfRepositoryMetadata['NumberOfMerges'].max()
print(f"Valore minimo in 'NumberOfMerges': {min_value}")
print(f"Valore massimo in 'NumberOfMerges': {max_value}")

# Definiamo i bin e le etichette
bin_edges = [0, 0.99999999, 10, 25, 50, 100, 200, 300, 400, 500, np.inf]
bin_labels = ['[0]', '(0,10]', '(10,25]', '(25,50]', '(50,100]', '(100,200]', '(200,300]', '(300,400]', '(400,500]', '(500+]']

# Crea una distribuzione dei dati usando pd.cut con i bin definiti
barChartData = pd.cut(dfRepositoryMetadata['NumberOfMerges'], bins=bin_edges, labels=bin_labels, include_lowest=True)

# Conta il numero di repository per ciascun intervallo
barChartCounts = barChartData.value_counts().sort_index()

# Verifica se ci sono repository fuori intervallo che dovrebbero essere inclusi
num_out_of_bounds = len(dfRepositoryMetadata) - len(barChartData.dropna())
if num_out_of_bounds > 0:
    # Aggiungi i repository fuori intervallo a '[500+]' se non esistono ancora
    if '[500+]' in barChartCounts.index:
        barChartCounts['[500+]'] += num_out_of_bounds
    else:
        barChartCounts['[500+]'] = num_out_of_bounds

# Verifica il numero totale di repository per ciascun intervallo
print("Conteggio dei repository per intervallo:")
print(barChartCounts)
print(f"Somma dei conteggi: {barChartCounts.sum()}")

# Crea un grafico a barre per visualizzare la distribuzione
plt.figure(figsize=(12, 6))
barChart = barChartCounts.plot.bar(color="green", edgecolor='black')

# Adatta l'asse y ai dati
plt.ylim(0, barChartCounts.max() + 500)  # Aumenta il limite superiore per mostrare tutti i dati

# Aggiungi etichette al grafico
plt.xticks(rotation=45)
plt.xlabel('Number of Merges')
plt.ylabel('Number of Repositories')

barChart.bar_label(barChart.containers[0])

# Mostra il grafico
plt.tight_layout()  # Assicura che tutto il layout venga visualizzato correttamente
plt.show()
