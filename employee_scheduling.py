import pandas as pd
import numpy as np


df = pd.read_csv("holiday_schedule.csv",delimiter=',')
print(df.head())
df_new = pd.DataFrame(columns=df.columns)

col_index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in df.index:
    for j in col_index:
        if df.iat[i,j] == 1:
            df_new.append({df.Employee,df.ait[i,j]})
print(df_new.head())

"""
    for i in df.index:
        if df.iloc[i,col.index] == 1:
            df_new.append({df.iloc[i,col.index],'X'})

print(df_new.head())
"""