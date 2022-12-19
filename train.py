import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb

df = pd.read_csv('Data.csv')
df = df.drop(columns=['prev_address_months_count'])
df['current_address_months_count'] = df['current_address_months_count'].replace(-1, 0)
df['bank_months_count'] = df['bank_months_count'].replace(-1, df['bank_months_count'].loc[df['bank_months_count'] != -1].median())
df['device_distinct_emails_8w'] = df['device_distinct_emails_8w'].replace(-1, df.mode()['device_distinct_emails_8w'][0])
df['session_length_in_minutes'] = df['session_length_in_minutes'].replace(-1, df['session_length_in_minutes'].median())
X = df.drop(columns=['fraud_bool'])
y = df['fraud_bool']
dicts = X.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)
X_full_train, X_test, y_full_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_full_train, y_full_train, test_size=0.25, random_state=42)
dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=dv.get_feature_names())
dval = xgb.DMatrix(X_val, label=y_val, feature_names=dv.get_feature_names())
xgb_params = {
    'eta': 0.4,
    'max_depth': 2,
    'colsample_bytree': 0.8,
    'subsample': 1,
    'min_child_weight': 1.5,
    'gamma': 0.4,
    'lambda': 10,

    'objective': 'binary:logistic',
    'nthread': 8,
    'eval_metric': 'auc',
    'seed': 42,
    'verbosity': 1,
}
model = xgb.train(xgb_params, dtrain, evals=watchlist, num_boost_round=100)
print(bentoml.xgboost.save_model("fraud_detection_model", model, custom_objects={"dictVectorizer": dv}))