import pandas as pd
import numpy as np
df=pd.read_csv('/Users/PRATYAY/Downloads/CausesOfDeath_France_2001-2008.csv')
print(df)
print("Number of missing data is: ")
print(df.isnull().sum().sum())
print(df.isnull().sum())
print("Number of filled data is: ")
print(df.notnull().sum().sum())
print(df.describe())
df['Value'].fillna(994, inplace=True)
print(df)





