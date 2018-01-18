#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 01:24:01 2018

@author: sahebsingh
"""

import pandas as pd
import numpy as np


df = pd.read_csv('/Users/sahebsingh/Desktop/Projects/books/Mastering/Data/census_test.csv')
#print(df.info())

# Getting the total percentage of values filled 
percentage_fill = df.count(0)/df.shape[0] * 100
#print(percentage_fill) # Will give the total number of values present.

# Removing Null Values
df = df.dropna(how = 'any')
del df['education_num']

# Exploring the Data Census Data

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Hypothesis 1: People who are older earn more.

# People earning more than 50k per year
df_above_50k = df[df['greater_than_50k'] == 1]
plt.hist(df_above_50k['age'])
plt.ylabel('Frequency')
plt.xlabel("Age")
plt.show()

# People earning less than 50k per year
df_below_50k = df[df['greater_than_50k'] == 0]
plt.hist(df_below_50k['age'])
plt.ylabel("Frequency")
plt.xlabel('Age')
plt.show()


# Hypothesis 2: Income is based on working class.

percentage = df_above_50k.groupby('workclass').workclass.count()
percentage = percentage.sort_values(ascending = False)
total = sum(percentage.values)
percentage = percentage/total
ax = percentage.plot(kind = 'bar', color = 'r')
ax.set_ylabel('Percentage')
plt.show()












