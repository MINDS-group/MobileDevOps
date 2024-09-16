import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics

csvFile = pd.read_csv('./Queries/Query/Q2/Q2_days.csv', sep=',', names=['RepositoryName','CommitId','CommitDatetime','FirstReleaseBeforeCommit','ReleaseBeforeDatetime',
                      'MillisecondsBeforeCommit','FirstReleaseAfterCommit','ReleaseAfterDatetime','MillisecondsAfterCommit'],
                      skiprows=1)

dfCsv = pd.DataFrame(csvFile)

distancesFromReleaseBefore = dfCsv["MillisecondsBeforeCommit"].replace(0, np.nan).dropna().to_numpy()

dfRepositories = dfCsv["RepositoryName"].drop_duplicates(keep='first')
dfRepositories = pd.DataFrame(dfRepositories)

medianTimeDistanceList = []

for i,row in dfRepositories.iterrows():
    
    currentRepo = row["RepositoryName"]

    commits = dfCsv.query('RepositoryName == @currentRepo')

    timeDistances = commits["MillisecondsBeforeCommit"].values

    dfTimeDistances = pd.DataFrame(timeDistances).replace(0,np.nan).dropna()
    timeDistances = dfTimeDistances[0].tolist()

    if(len(timeDistances) > 0):

        medianTimeDistance = statistics.median(timeDistances)

        medianTimeDistanceList.append(medianTimeDistance)
    else:
        continue

fig, ax = plt.subplots(1, figsize=(11, 7))

box1 = plt.boxplot([distancesFromReleaseBefore, medianTimeDistanceList], showfliers=False)

plt.grid(axis='y')

plt.title("Time Distance Distribution From Previous Release")
plt.ylabel('Time Distance (Days)') 
x = np.array([1,2])
my_xticks = ['For Commit','For Repository']
plt.xticks(x, my_xticks)

for line in box1['medians']:
    (x_l, y),(x_r, _) = line.get_xydata()
    if not np.isnan(y): 
        x_line_center = x_l + (x_r - x_l)+0.01
        y_line_center = y  
        ax.text(x_line_center, y_line_center, 
                '%.2f' % y, 
                verticalalignment='center',
                fontsize=8)
     
for line in box1['whiskers']:    
    (x_l, y),(x_r, _) = line.get_xydata()
    if not np.isnan(y): 
        x_line_center = (x_l + (x_r - x_l)/1.2)-0.21
        y_line_center = y+0.02 
        ax.text(x_line_center, y_line_center,
                '%.2f' % y, 
                verticalalignment='center',
                fontsize=8)

for line in box1['caps']:    
    (x_l, y),(x_r, _) = line.get_xydata()
    if not np.isnan(y): 
        x_line_center = (x_l + (x_r - x_l)/1.2)-0.21
        y_line_center = y+0.02 
        ax.text(x_line_center, y_line_center,
                '%.2f' % y, 
                verticalalignment='center',
                fontsize=8)
plt.show()


