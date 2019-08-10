import numpy as np
import pandas as pd
import os

print('Current Working Directory: ' ,os.getcwd())
df_train = pd.read_csv('./challenge_data/train.csv')
df_labels = pd.read_excel('./challenge_data/Hypothesis.xlsx', sheet_name='Sheet1', header=4)
print(df_labels.head(10))
# print(df_train.columns)
# print(df_labels.columns)