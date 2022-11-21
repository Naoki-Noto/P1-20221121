#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:42:24 2021

@author: notonaoki
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import LeaveOneOut


columns = ['bad', 'good', 'very_good']
columns2 = ['AS']
columns3 = ['F1_macro']

data = pd.read_csv('data_hybrid_descriptors.csv') # for hybrid descriptors
#data = pd.read_csv('data_RDKit_descriptors.csv')  # for RDKit descriptors
#data = pd.read_csv('data_DFT_descriptors.csv')    # for DFT descriptors
y = pd.DataFrame(data['Class'],columns=['Class'])

X = data.drop(columns=['Name', 'id', 'Yield_2h', 'Yield_12h', 'Class'])

data_RS1 = []
data_PS1 = []
data_F11 = []
data_F1_macro1 = []
data_AS1 = []
data_RS2 = []
data_PS2 = []
data_F12 = []
data_F1_macro2 = []
data_AS2 = []
for i in range(0,100):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=18, random_state=i, stratify=y)
    print(X_test)
    
    loo = LeaveOneOut()
    param_grid = {'max_depth':[1,2,3,4,5],'n_estimators': list(range(100, 1001, 100))}
    clf_rf = GridSearchCV(RandomForestClassifier(random_state=0), param_grid=param_grid, scoring='accuracy', cv=loo, n_jobs=8)
    clf_rf.fit(X_train,y_train['Class'])
    clf_best = clf_rf.best_estimator_
    y_pred1 = clf_best.predict(X_train)
    y_pred2 = clf_best.predict(X_test)
    #train
    AS1 = accuracy_score(y_train, y_pred1)
    RS1 = recall_score(y_train, y_pred1, average=None)
    PS1 = precision_score(y_train, y_pred1, average=None)
    F11 = f1_score(y_train, y_pred1, average=None)
    F1_macro1 = f1_score(y_train, y_pred1, average='macro')
    #test
    AS2 = accuracy_score(y_test, y_pred2)
    RS2 = recall_score(y_test, y_pred2, average=None)
    PS2 = precision_score(y_test, y_pred2, average=None)
    F12 = f1_score(y_test, y_pred2, average=None)
    F1_macro2 = f1_score(y_test, y_pred2, average='macro')
    print(classification_report(y_test, y_pred2))

    data_RS1.append(RS1)
    data_PS1.append(PS1)
    data_F11.append(F11)
    data_F1_macro1.append(F1_macro1)
    list_AS1 = [AS1]
    data_AS1.append(list_AS1)
    
    data_RS2.append(RS2)
    data_PS2.append(PS2)
    data_F12.append(F12)
    data_F1_macro2.append(F1_macro2)
    list_AS2 = [AS2]
    data_AS2.append(list_AS2)

data_RS1 = pd.DataFrame(data=data_RS1, columns=columns)
data_PS1 = pd.DataFrame(data=data_PS1, columns=columns)
data_F11 = pd.DataFrame(data=data_F11, columns=columns)
data_F1_macro1 = pd.DataFrame(data=data_F1_macro1, columns=columns3)
data_AS1 = pd.DataFrame(data=data_AS1, columns=columns2)
data_RS2 = pd.DataFrame(data=data_RS2, columns=columns)
data_PS2 = pd.DataFrame(data=data_PS2, columns=columns)
data_F12 = pd.DataFrame(data=data_F12, columns=columns)
data_F1_macro2 = pd.DataFrame(data=data_F1_macro2, columns=columns3)
data_AS2 = pd.DataFrame(data=data_AS2, columns=columns2)
print('train')
print(data_RS1)
print(data_PS1)
print(data_F11)
print(data_F1_macro1)
print(data_AS1)
print('test')
print(data_RS2)
print(data_PS2)
print(data_F12)
print(data_F1_macro2)
print(data_AS2)

# hybrid descriptors
data_RS1.to_csv('result/hybrid/RF/RS_train.csv')
data_PS1.to_csv('result/hybrid/RF/PS_train.csv')
data_F11.to_csv('result/hybrid/RF/F1_train.csv')
data_F1_macro1.to_csv('result/hybrid/RF/F1_macro_train.csv')
data_AS1.to_csv('result/hybrid/RF/AS_train.csv')

data_RS2.to_csv('result/hybrid/RF/RS_test.csv')
data_PS2.to_csv('result/hybrid/RF/PS_test.csv')
data_F12.to_csv('result/hybrid/RF/F1_test.csv')
data_F1_macro2.to_csv('result/hybrid/RF/F1_macro_test.csv')
data_AS2.to_csv('result/hybrid/RF/AS_test.csv')

# RDKit descriptors
"""data_RS1.to_csv('result/RDKit_RF/RS_train.csv')
data_PS1.to_csv('result/RDKit_RF/PS_train.csv')
data_F11.to_csv('result/RDKit_RF/F1_train.csv')
data_F1_macro1.to_csv('result/RDKit_RF/F1_macro_train.csv')
data_AS1.to_csv('result/RDKit_RF/AS_train.csv')

data_RS2.to_csv('result/RDKit_RF/RS_test.csv')
data_PS2.to_csv('result/RDKit_RF/PS_test.csv')
data_F12.to_csv('result/RDKit_RF/F1_test.csv')
data_F1_macro2.to_csv('result/RDKit_RF/F1_macro_test.csv')
data_AS2.to_csv('result/RDKit_RF/AS_test.csv')"""

# DFT descriptors
"""data_RS1.to_csv('result/DFT_RF/RS_train.csv')
data_PS1.to_csv('result/DFT_RF/PS_train.csv')
data_F11.to_csv('result/DFT_RF/F1_train.csv')
data_F1_macro1.to_csv('result/DFT_RF/F1_macro_train.csv')
data_AS1.to_csv('result/DFT_RF/AS_train.csv')

data_RS2.to_csv('result/DFT_RF/RS_test.csv')
data_PS2.to_csv('result/DFT_RF/PS_test.csv')
data_F12.to_csv('result/DFT_RF/F1_test.csv')
data_F1_macro2.to_csv('result/DFT_RF/F1_macro_test.csv')
data_AS2.to_csv('result/DFT_RF/AS_test.csv')"""


