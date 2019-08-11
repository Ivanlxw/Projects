import numpy as np
import pandas as pd

train = pd.read_csv('./challenge_data/train.csv')
truth = pd.read_csv('./challenge_data/test_blank.csv')

def get_xy(df):
    df = df.drop(['Time Period'], axis=1)
    X = df.drop(['Value'], axis=1)
    y = df['Value']
    return X,y

X,y = get_xy(train)
X_truth, y_truth = get_xy(df=truth)

#One-hot encode
X = pd.get_dummies(X)
X_truth = pd.get_dummies(X_truth)
#same for ground truth
X_merged = pd.concat([X_truth,X], sort=False)
X_merged

X_truth_filter = X_merged['Generic LookupKey_ConsumerSandesh Brand 1BroadbandAllComplaints Regulator'].isna()
X_filter = [not item for item in X_truth_filter]

X = X_merged[X_filter].fillna(0)
X_truth = X_merged[X_truth_filter].fillna(0)


from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,r2_score

#split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

def training_best_param(X_train, X_test, y_train, y_test):
    param_grid = {'n_estimators' : [2,10,20,50],
                  'min_samples_split': [2,5,10,30],
                  'min_samples_leaf': [10,20,50,100],
                  'warm_start': [True, False]}

    grid = GridSearchCV(RandomForestRegressor(), param_grid, verbose=2, scoring='neg_mean_absolute_error')
    grid.fit(X_train, y_train)
    print(grid.best_params_)
    y_pred = grid.predict(X_test)

    #RETURNS R2-SCORE
    print("R^2 score: ", r2_score(y_test, y_pred))
    print("MAE: ", mean_absolute_error(y_test,y_pred))

    return {'params': grid.best_params_,'metrics': [r2_score(y_test, y_pred), mean_absolute_error(y_test, y_pred)]}

def training_model(best_params):

        #split dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

        param_n_estimators =  best_params['min_samples_leaf']
        param_min_samples_split = best_params['min_samples_split']
        param_min_samples_leaf = best_params['min_samples_leaf']
        param_warm_start = best_params['warm_start']

        model = RandomForestRegressor(n_estimators = param_n_estimators,
                                      min_samples_split= param_min_samples_split,
                                      min_samples_leaf = param_min_samples_leaf,
                                      warm_start = param_warm_start)
        model.fit(X_train,y_train)
        return model

best_params = training_best_param(X_train, X_test, y_train, y_test)
model = training_model(best_params['params'])


y_truth = model.predict(X_truth)
truth['Value'] = y_truth

#evaluation
from sklearn.metrics import mean_absolute_error, r2_score
error = mean_absolute_error(y_test, model.predict(X_test))
r2 = r2_score(y_test, model.predict(X_test))

truth.to_csv('./challenge_data/test_filled.csv')
