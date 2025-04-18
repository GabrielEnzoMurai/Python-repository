# -*- coding: utf-8 -*-
"""desafio6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MvyOrMOh2VkESOOHq53vBeFhrUEEwgy-
"""

çoimport pandas as pd
import seaborn as sns
import numpy as np

"""Data Understanting"""

df = pd.read_csv("streaming_data.csv")
df.head()

df.info()

df.isna().sum()

"""Colunas com null: Age, Gender, Time_on_plataform, Devices_connected, Subscription_type, Num_streaming_services, Avg_rating, Churned

Data Preparation
"""

df[['Time_on_platform', 'Num_streaming_services', 'Churned', 'Avg_rating', 'Devices_connected']] = df[['Time_on_platform', 'Num_streaming_services', 'Churned', 'Avg_rating', 'Devices_connected']].fillna(0)

df.isna().sum()

"""Colunas com null: Age, Gender, Subscription_type"""

df.dropna(inplace=True)

df.isna().sum()

df['Churned'] = df['Churned'].replace(1, 'Yes')
df['Churned'] = df['Churned'].replace(0, 'No')

df.head()

df.dtypes

df[['Age', 'Time_on_platform', 'Devices_connected', 'Num_streaming_services', 'Avg_rating']] = df[['Age', 'Time_on_platform', 'Devices_connected', 'Num_streaming_services', 'Avg_rating']].astype('int64')

df.dtypes

"""Modelagem de Dados"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import (accuracy_score,
                             confusion_matrix,
                             recall_score,
                             precision_score)
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

cols_drop = df[['Churned', 'User_id']]

X = df.drop((cols_drop), axis=1)

y = df['Churned']

le = LabelEncoder()

le.fit(X.Gender)
X.Gender = le.transform(X.Gender)

le.fit(X.Subscription_type)
X.Subscription_type = le.transform(X.Subscription_type)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)

X.head()

scaler = MinMaxScaler()

scaler.fit(X)
scaler.transform(X_train)
scaler.transform(X_test)

X_train.head()

lr = LogisticRegression()

lr.fit(X_train, y_train)

lr.predict(X_test)

X_test.assign(churn=y_test).assign(labe=lr.predict(X_test))

from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_estimator(lr, X_test, y_test)

from sklearn.metrics import accuracy_score

print(f"Acurácia (Treino): {accuracy_score(y_train, lr.predict(X_train))}")
print(f"Acurácia (Teste): {accuracy_score(y_test, lr.predict(X_test))}")

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()

rf.fit(X_train, y_train)

ConfusionMatrixDisplay.from_estimator(rf, X_test, y_test)

print(f"Acurácia (Treino): {accuracy_score(y_train, rf.predict(X_train))}")
print(f"Acurácia (Teste): {accuracy_score(y_test, rf.predict(X_test))}")

from sklearn.model_selection import GridSearchCV

parameters = {'max_depth': [1,2,3,4,5,6,7,8,9,10],
              'n_estimators': [100, 300, 500]}

grid_search = GridSearchCV(rf, parameters, scoring="accuracy", cv=5, n_jobs=-1)

grid_search.fit(X_train, y_train)

grid_search.best_estimator_.get_params()

rf_tunned = RandomForestClassifier(bootstrap = True,
    ccp_alpha = 0.0,
    class_weight = None,
    criterion = 'gini',
    max_depth = 10,
    max_features = 'sqrt',
    max_leaf_nodes = None,
    max_samples = None,
    min_impurity_decrease = 0.0,
    min_samples_leaf = 1,
    min_samples_split = 2,
    min_weight_fraction_leaf = 0.0,
    monotonic_cst = None,
    n_estimators = 100,
    n_jobs = None,
    oob_score = False,
    random_state = None,
    verbose = 0,
    warm_start = False)

rf_tunned

rf_tunned.fit(X_train, y_train)

rf_tunned.predict(X_test)

X_test.assign(churn=y_test).assign(label=rf_tunned.predict(X_test))

ConfusionMatrixDisplay.from_estimator(rf_tunned, X_test, y_test)

print(f"Acurácia (Treino): {accuracy_score(y_train, rf_tunned.predict(X_train))}")
print(f"Acurácia (Teste): {accuracy_score(y_test, rf_tunned.predict(X_test))}")