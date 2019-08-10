import numpy as np
import pandas as pd
import os

print('Current Working Directory: ' ,os.getcwd())
df_train = pd.read_csv('./challenge_data/train.csv')
df_labels = pd.read_excel('./challenge_data/Hypothesis.xlsx', sheet_name='Sheet1', header=3)
print(df_labels.head(10))
df_labels = df_labels.rename(columns={df_labels.columns[3]:df_train.columns[3], df_labels.columns[4]:df_train.columns[4]})
print(df_train.columns)
print(df_labels.columns)
df_final = pd.merge(df_train, df_labels, on=['Generic Group', 'Generic Brand', 'Generic Product Category', 'Generic Product', 'Variable Group','Generic Variable','Generic LookupKey'])
df_final.columns

# Sorting dataframe to better look at dataframe
df_final = df_final.sort_values(by=['Time Period'])
df_final
