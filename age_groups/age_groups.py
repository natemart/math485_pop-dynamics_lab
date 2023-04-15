import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load data
cenPop = {
    2010 : pd.read_csv('./2010.csv', header=0, skiprows=[1], skip_blank_lines=True, dtype={'Age':str, 'Both sexes':float, 'Both sexes.1': float, 'Male':float, 'Male.1':float, 'Female':float, 'Female.1':float}),
    2011 : pd.read_csv('./2011.csv', header=0, skiprows=[1], skip_blank_lines=True, dtype={'Age':str, 'Both sexes':float, 'Both sexes.1': float, 'Male':float, 'Male.1':float, 'Female':float, 'Female.1':float}),
    2012 : pd.read_csv('./2012.csv', header=0, skiprows=[1], skip_blank_lines=True, dtype={'Age':str, 'Both sexes':float, 'Both sexes.1': float, 'Male':float, 'Male.1':float, 'Female':float, 'Female.1':float}),
    2013 : pd.read_csv('./2013.csv', header=0, skiprows=[1], skip_blank_lines=True, dtype={'Age':str, 'Both sexes':float, 'Both sexes.1': float, 'Male':float, 'Male.1':float, 'Female':float, 'Female.1':float}),
    2014 : pd.read_csv('./2014.csv', header=0, skiprows=[1], skip_blank_lines=True, dtype={'Age':str, 'Both sexes':float, 'Both sexes.1': float, 'Male':float, 'Male.1':float, 'Female':float, 'Female.1':float}),
    2015 : pd.read_csv('./2015.csv', header=0, skiprows=[1], skip_blank_lines=True, dtype={'Age':str, 'Both sexes':float, 'Both sexes.1': float, 'Male':float, 'Male.1':float, 'Female':float, 'Female.1':float}),
    2016 : pd.read_csv('./2016.csv', header=0, skiprows=[1], skip_blank_lines=True, dtype={'Age':str, 'Both sexes':float, 'Both sexes.1': float, 'Male':float, 'Male.1':float, 'Female':float, 'Female.1':float}),
    2017 : pd.read_csv('./2017.csv', header=0, skiprows=[1], skip_blank_lines=True, dtype={'Age':str, 'Both sexes':float, 'Both sexes.1': float, 'Male':float, 'Male.1':float, 'Female':float, 'Female.1':float}),
    2018 : pd.read_csv('./2018.csv', header=0, skiprows=[1], skip_blank_lines=True, dtype={'Age':str, 'Both sexes':float, 'Both sexes.1': float, 'Male':float, 'Male.1':float, 'Female':float, 'Female.1':float}),
    2019 : pd.read_csv('./2019.csv', header=0, skiprows=[1], skip_blank_lines=True, dtype={'Age':str, 'Both sexes':float, 'Both sexes.1': float, 'Male':float, 'Male.1':float, 'Female':float, 'Female.1':float})
    }


main_data = {yr : (cenPop[yr].iloc[1:4, :]['Both sexes'].sum(), cenPop[yr].iloc[4:10, :]['Both sexes'].sum(), cenPop[yr].iloc[10:19, :]['Both sexes'].sum()) for yr in cenPop}




# group1: 0 - 14yrs, group2: 15 - 44 yrs, group3: 44+ yrs
grp1 = cenPop[2010].iloc[1:4, :]
grp2 = cenPop[2010].iloc[4:10, :]
grp3 = cenPop[2010].iloc[10:19, :]

# general fertility rate 2010 (gfr) per 1000 women ages 15 - 44
gfr2010 = 64.0 / 1000

# 2010 estimated birth rate
birthRate2010 = (gfr2010 * grp2['Female'].sum()) / grp2['Both sexes'].sum()

# death rates per 100,000 people
deathRate_grp1= (588.0 + 24.0 + 11.5 + 14.0) / 100000
deathRate_grp2 = (45.5 + 83.8 + 99.7 + 117.3 + 147.2 + 202.4) / 100000
deathRate_grp3 = (311.3 + 491.3 + 730.6 + 1032.2 + 1454.0 + 2246.1 + 3560.5 + 5944.6 + 13407.9) / 100000

# probability of movement of group1 to group2, and from group2 - group3
probGrp1_2 = 14 / grp1['Both sexes'].sum()
probGrp2_3 = (44 - 15) / grp2['Both sexes'].sum()

estimated_data = {2010: (grp1['Both sexes'].sum(), grp2['Both sexes'].sum(), grp3['Both sexes'].sum())} 
for i in cenPop:
    if i + 1 <= 2019:
        grp1 = estimated_data[i][0] + birthRate2010*estimated_data[i][1] - deathRate_grp1*estimated_data[i][0] - probGrp1_2*estimated_data[i][0]
        grp2 = estimated_data[i][1] + probGrp1_2*estimated_data[i][0] - deathRate_grp2*estimated_data[i][1] - probGrp2_3*estimated_data[i][1]
        grp3 = estimated_data[i][2] + probGrp2_3*estimated_data[i][1] - deathRate_grp3*estimated_data[i][2] 
        estimated_data[i + 1] = (grp1, grp2, grp3)
    else:
        break

comparison = {
    'main_grp1' : [main_data[yr][0] for yr in main_data],
    'est_grp1' : [estimated_data[yr][0] for yr in estimated_data],
    'main_grp2' : [main_data[yr][1] for yr in main_data],
    'est_grp2': [estimated_data[yr][1] for yr in estimated_data],
    'main_grp3' : [main_data[yr][2] for yr in main_data],
    'est_grp3' : [estimated_data[yr][2] for yr in estimated_data]
    }
    
x = np.arange(len(main_data))
width= 0.1
multiplier = 0
fig, ax = plt.subplots(layout='constrained')
for yr, groups in comparison.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, groups, width, label=yr)
    ax.bar_label(rects, padding=3)
    multiplier += 1


ax.set_ylabel('population size')
ax.set_xticks(x + width, np.arange(2010, 2020))
ax.legend(loc='upper left', ncols=6)

plt.show()








