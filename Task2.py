import pandas as pd
import numpy as np
df=pd.read_csv('/Users/PRATYAY/Downloads/CausesOfDeath_France_2001-2008.csv')
df
print("Number of missing data is: ")
print(df.isnull().sum().sum())
print(df.isnull().sum())
print("Number of filled data is: ")
print(df.notnull().sum().sum())
m1= df['Value'].mean()
df['Value'].fillna(m1, inplace=True)


