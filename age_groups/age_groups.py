import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cenPop = { 
    '2010' : pd.read_csv('./2010.csv', header=0, skiprows=[1], skip_blank_lines=True),
    '2011' : pd.read_csv('./2011.csv', header=0, skiprows=[1], skip_blank_lines=True),
    '2012' : pd.read_csv('./2012.csv', header=0, skiprows=[1], skip_blank_lines=True),
    '2013' : pd.read_csv('./2013.csv', header=0, skiprows=[1], skip_blank_lines=True),
    '2014' : pd.read_csv('./2014.csv', header=0, skiprows=[1], skip_blank_lines=True),
    '2015' : pd.read_csv('./2015.csv', header=0, skiprows=[1], skip_blank_lines=True),
    '2016' : pd.read_csv('./2016.csv', header=0, skiprows=[1], skip_blank_lines=True),
    '2017' : pd.read_csv('./2017.csv', header=0, skiprows=[1], skip_blank_lines=True),
    '2018' : pd.read_csv('./2018.csv', header=0, skiprows=[1], skip_blank_lines=True),
    '2019' : pd.read_csv('./2019.csv', header=0, skiprows=[1], skip_blank_lines=True)
    }


cen2010_0_14 = cenPop['2010'].iloc[2:5, :]
cen2010_15_44 = cenPop['2010'].iloc[5:11, :]
cen2010_45_over = cenPop['2010'].iloc[11:, :]

# general fertility rate 2010 (gfr) per 1000 women ages 15 - 44
b = 64.0

# death rates per 100,000 people
d0_14= 588.0 + 24.0 + 11.5 + 14.0
d15_44 = 45.5 + 83.8 + 99.7 + 117.3 + 147.2 + 202.4
d45_over = 377.3 + 491.3 + 730.6 + 1032.2 + 1454.0 + 2246.1 + 3560.5 + 5944.6 + 13407.9

# splitting 2010 census into age groups



