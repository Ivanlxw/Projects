import numpy as np
import pandas as pd

import os
# print('Current Working Directory: ' ,os.getcwd())

def mergesort_fcodata(df_train, df_labels):
    df_labels = df_labels.rename(columns={df_labels.columns[3]:df_train.columns[3], df_labels.columns[4]:df_train.columns[4]})
    df_final = pd.merge(df_train, df_labels, on=['Generic Group', 'Generic Brand', 'Generic Product Category', 'Generic Product', 'Variable Group','Generic Variable','Generic LookupKey'])
    df_final = df_final.sort_values(by=['Time Period'])
    return df_final

#read the raw data
df_train = pd.read_csv('./challenge_data/train.csv')
df_labels = pd.read_excel('./challenge_data/Hypothesis.xlsx', sheet_name='Sheet1', header=3)

# Sorting dataframe to better look at dataframe
df = mergesort_fcodata(df_train, df_labels)
print(df.columns)

"""
Feature Importance:
We'll fit a neural network to predict the features that drive a specific churn, gross adds, etc.

Steps Required:
1. Split into X and y
# X = product details and the 4 metrics to forecast
# y = Generic variable

2. One-hot encode
3. create validation set via train_test_split
4. Run the neural network
5. Predict via inputs

"""
X = df.drop(['Generic Variable', 'Data type', 'Value', 'Time Period', 'Generic Sub-Variable','Generic LookupKey'], axis=1)
y = df['Generic Variable']
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def label_encode(df,col, axis):
    if axis==0:
        labelencoder_X_col = LabelEncoder()
        df[col] = labelencoder_X_col.fit_transform(df[col])
        return df
    elif axis ==1:
        labelencoder_y = LabelEncoder()
        df = labelencoder_y.fit_transform(df)
        return df

for col in ['Generic Group', 'Generic Brand', 'Generic Product Category', 'Generic Product', 'Variable Group', 'Units']:
    X = label_encode(X, col, axis=0)

onehotencoder = OneHotEncoder(sparse=False)
X = onehotencoder.fit_transform(X)
print(X.shape)

y = pd.get_dummies(y)
print(y.shape)

import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout,PReLU


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


classifier = Sequential()
classifier.add(Dense(units = 250, kernel_initializer="random_normal", input_dim=47))
classifier.add(Dropout(0.2))
classifier.add(keras.layers.PReLU())
classifier.add(Dense(units = 150, kernel_initializer="random_normal"))
classifier.add(Dropout(0.2))
classifier.add(keras.layers.PReLU())

classifier.add(Dense(units= 74, kernel_initializer="random_normal", activation='softmax'))

classifier.compile(optimizer = 'adam', loss='categorical_crossentropy', metrics=['accuracy'])
classifier.fit(X_train, y_train, batch_size=32, epochs=500)

y_pred = classifier.predict(X_test)

def predict_topk(array,k):
    topk = np.argsort(array)[(-1*k):]
    print(topk)
    return y.columns[topk]

def trainsform_top(array):
    n = np.argmax(array)
    array = [0 for i in range(array.size)]
    array[n] = 1
    return array

y_ans = np.array([trainsform_top(y_pred[i]) for i in range(y_pred.shape[0])])

y_ans.shape
y_test.shape

from sklearn.metrics import accuracy_score, classification_report
cr = accuracy_score(y_test, y_ans)
print(cr)
