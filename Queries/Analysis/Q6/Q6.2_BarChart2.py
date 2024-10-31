import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csvFile = pd.read_csv('./Queries/Analysis/Q6/Q6.csv', sep=',', names=['RepositoryName', 'NumOfContributors', 'Contributor', '%OfContribution'],
                      skiprows=1)

dfCsv = pd.DataFrame(csvFile)

contributionsDf = dfCsv["%OfContribution"].to_numpy()

# Definisci i bin senza np.inf e correggi l'ultima etichetta
bin_edges = [0, 1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99.999999999, np.inf]
bin_labels = ['[0,1%]', '(1,2%]', '(2,5%]', '(5,10%]', '(10,20%]', '(20,30%]', '(30,40%]', 
              '(40,50%]', '(50,60%]', '(60,70%]', '(70,80%]', '(80,90%]', '(90,100%)', '[100]']

# Crea i tagli sui dati
barChartData = pd.cut(contributionsDf, bins=bin_edges, labels=bin_labels, include_lowest=True)

# Conta il numero di contributori per ciascun intervallo
barChartCounts = barChartData.value_counts().sort_index()

# Crea il grafico
barChart = barChartCounts.plot.bar(color="green")

# Aggiungi etichette
plt.xticks(rotation=45)
#plt.title("Distribution Of Contribution Percentages")
plt.xlabel('Contribution Percentage') 
plt.ylabel('Number of Contributors')

barChart.bar_label(barChart.containers[0])

# Mostra il grafico
plt.show()
