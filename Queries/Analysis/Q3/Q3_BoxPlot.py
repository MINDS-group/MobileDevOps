import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csvFile = pd.read_csv('./Queries/Query/Q3/Q3.csv', sep=',', names=['RepositoryName','NumOfReleases', 'ReleaseFrequency (days)'],
                      skiprows=1)

df = pd.DataFrame(csvFile)

releasesFrequency = df["ReleaseFrequency (days)"].replace(0, np.nan).dropna().to_numpy()

fig, ax = plt.subplots(1, figsize=(11, 7))

box1 = plt.boxplot([releasesFrequency],showfliers=False)

plt.title("Release Frequency For Repository")
plt.ylabel('Release Frequency (Days)') 
x = np.array([1])
my_xticks = ['Percentage Of Repositories']
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
        x_line_center = (x_l + (x_r - x_l)/1.2)-0.15
        y_line_center = y+0.02 
        ax.text(x_line_center, y_line_center,
                '%.2f' % y, 
                verticalalignment='center',
                fontsize=8)
      
for line in box1['caps']:    
    (x_l, y),(x_r, _) = line.get_xydata()
    if not np.isnan(y): 
        x_line_center = (x_l + (x_r - x_l)/1.2)+0.02
        y_line_center = y+0.02 
        ax.text(x_line_center, y_line_center,
                '%.2f' % y, 
                verticalalignment='center',
                fontsize=8)
        
plt.show()


