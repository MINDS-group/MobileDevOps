import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csvFile = pd.read_csv('./Queries/Query/Q4/Q4.csv', sep=',', names=['RepositoryName','CommitId', 'NumOfModifiedFiles'],
                      skiprows=1)

dfCsv = pd.DataFrame(csvFile)

modifiedFilesDf = dfCsv["NumOfModifiedFiles"].dropna().to_numpy()

barChartData = pd.cut(modifiedFilesDf, [0,3,6,10,np.inf], labels=['0-2','3-5','6-9','10+'])
barChart = barChartData.value_counts().plot.bar(color="green")

plt.xticks(rotation=0)
plt.title("Distribution of Modified Files by Commit")
plt.xlabel('Number Of Modified Files')
plt.ylabel('Number Of Commit')

barChart.bar_label(barChart.containers[0])

plt.show()


