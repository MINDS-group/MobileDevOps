import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csvFile = pd.read_csv('./Queries/Analysis/Q6/Q6.csv', sep=',', names=['RepositoryName','NumOfContributors', 'Contributor', '%OfContribution'],
                      skiprows=1)

dfCsv = pd.DataFrame(csvFile)

contributionsDf = dfCsv["%OfContribution"].to_numpy()

barChartData = pd.cut(contributionsDf, [0,1,2,5,10,20,30,40,50,60,70,80,90,np.inf], labels=['[0%]','[1,2%]','[3,5%]','[6,10%]','[11,20%]','[21,30%]','[31,40%]','[41,50%]','[51,60%]','[61,70%]','[71,80%]','[81,90%]','[90,100%]'] )
barChart = barChartData.value_counts().plot.bar(color="green")

plt.xticks(rotation=45)
plt.title("Distribution Of Contribution Percentages")
plt.xlabel('Contribution Percentage') 
plt.ylabel('Number of Contributors')

barChart.bar_label(barChart.containers[0])

plt.show()


