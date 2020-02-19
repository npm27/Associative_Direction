##set up
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dat = pd.read_csv("POOLED BAR.csv")

#make the 95% confidence intervals
dat['diff'] = dat['Upper'].sub(dat['Lower']) #get the length of the bars
dat['diff2'] = dat['diff'].div(2) #length from line to point

##set up the initial plot
fig = plt.figure()
fig.set_size_inches(10,10)

ax1 = fig.add_subplot(1, 1, 1)

#subset by task
j1 = dat[dat['Task'] == 'JOL']
r1 = dat[dat['Task'] == 'Recall']

#get all the things to plug into the plots
#separate out averages and conf interval
j1_average = j1['Average']
r1_average = r1['Average']

j1_conf = j1['diff2']
r1_conf = r1['diff2']

ind = np.arange(len(j1_average))  # the x locations for the groups
width = 0.35 #bar width 

rects1 = ax1.bar(ind - width/2, j1_average, width, yerr = j1_conf, capsize = 3, color = 'white', edgecolor = 'k',
                label ='JOL')

rects2 = ax1.bar(ind + width/2, r1_average, width, yerr = r1_conf, capsize = 3, color = 'grey', edgecolor = 'k',
                label = 'Recall')

#Make the plot spiffy
ax1.set_title('Pooled Analysis', fontsize = 20, fontweight = 'bold')
ax1.set_ylabel('Mean % JOL/Recall', fontsize = 18, fontweight = 'bold')
ax1.set_xlabel('Direction', fontsize = 18, fontweight = 'bold')
#ax1.xaxis.labelpad = 0
ax1.set_xticks(ind)
ax1.set_xticklabels(('Backward', 'Forward', 'Symmetrical', 'Unrelated'), fontsize = 16)
ax1.legend(fontsize = 16)
ax1.set_ylim([0,100])

##save figure
fig.savefig('pooled_bar_chart.png', dip = 10000)
