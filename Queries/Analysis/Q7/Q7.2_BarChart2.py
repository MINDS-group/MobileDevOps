import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leggi il file CSV
csvFile = pd.read_csv('./Queries/Analysis/Q7/Q7.csv', sep=',', names=['RepositoryName', 'NumOfPullRequests', 'NumOfForks'], skiprows=1)

# Converti la colonna 'NumOfForks' in numerica, forzando i valori non numerici a NaN
csvFile['NumOfForks'] = pd.to_numeric(csvFile['NumOfForks'], errors='coerce')

# Verifica il numero totale di repository nel dataset originale
total_repositories_original = len(csvFile)
print(f"Totale repository nel dataset originale: {total_repositories_original}")

# Controlla il numero di repository con valori NaN
num_na = csvFile['NumOfForks'].isna().sum()
print(f"Numero di repository con valori NaN in 'NumOfForks': {num_na}")

# Verifica la gamma di valori
min_value = csvFile['NumOfForks'].min()
max_value = csvFile['NumOfForks'].max()
print(f"Valore minimo in 'NumOfForks': {min_value}")
print(f"Valore massimo in 'NumOfForks': {max_value}")

# Definiamo i bin e le etichette
bin_edges = [0, 0.999999999999, 10, 25, 50, 100, 200, 300, 400, 500, np.inf]
bin_labels = ['[0]', '(0,10]', '(10,25]', '(25,50]', '(50,100]', '(100,200]', '(200,300]', '(300,400]', '(400,500]', '(500+]']

# FORK: CHIARIRE IL NUMERO ALTO DI FORK (5600,3000)

# Crea una distribuzione dei dati usando pd.cut con i bin definiti
barChartData = pd.cut(csvFile['NumOfForks'], bins=bin_edges, labels=bin_labels, include_lowest=True)

# Conta il numero di repository per ciascun intervallo
barChartCounts = barChartData.value_counts().sort_index()

# Verifica se ci sono repository fuori intervallo che dovrebbero essere inclusi
num_out_of_bounds = len(csvFile) - len(barChartData.dropna())
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
barChart = barChartCounts.plot.bar(color="green")

# Adatta l'asse y ai dati
plt.ylim(0, barChartCounts.max() + 500)  # Aumenta il limite superiore per mostrare tutti i dati

# Aggiungi etichette al grafico
plt.xticks(rotation=45)
plt.xlabel('Number of Forks')
plt.ylabel('Number of Repositories')

barChart.bar_label(barChart.containers[0])

# Mostra il grafico
plt.show()
