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
print(percentage)
ax = percentage.plot(kind = 'bar', color = 'r')
ax.set_ylabel('Percentage')
plt.show()


# Hypothesis 3: Educated People Tend to Earn More

educated = df_above_50k.groupby('education').education.count()
educated = educated.sort_values(ascending = False)
total = sum(educated.values)
percentage_educated = educated/total
ax = percentage_educated.plot(kind = 'bar', color = 'b')
ax.set_ylabel("Percentage")
plt.show()

# Hypothesis 4: Married People Tend to Earn More

married = df_above_50k.groupby('marital_status').marital_status.count()
married = married.sort_values(ascending = False)
total = sum(married.values)
percentage_married = married/total
percentage_married.plot(kind = 'bar', color = 'r')
plt.ylabel('Percentage')
plt.xlabel('Marital Status')
plt.show()

# Hypothesis 5: There is a bias based on on race.

race = df_above_50k.groupby('race').race.count()
race = race.sort_values(ascending = False)
total = sum(race.values)
percentage_race = race/total
percentage_race.plot(kind = 'bar', color = 'b')
plt.ylabel('Percentage')
plt.xlabel('Race')
plt.show()

# Hypothesis 6: Income is based upon different of Occupations

occupations = df_above_50k.groupby('workclass').workclass.count()
occupations = occupations.sort_values(ascending = False)
total = sum(occupations.values)
percentage_occupation = occupations/total
percentage_occupation.plot(kind = 'bar', color = 'r')
plt.ylabel('Percentage')
plt.xlabel("Occupations")


















