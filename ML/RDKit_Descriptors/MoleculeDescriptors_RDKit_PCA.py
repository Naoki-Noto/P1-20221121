#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 09:12:43 2021

@author: notonaoki
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


data = pd.read_csv('data/MoleculeDescriptors.csv')

print(data)
X = np.array(data)
#print(X)
# PCA
sc = StandardScaler()
X_sc = sc.fit(X).transform(X)
#print(X_sc)
pca = PCA(n_components=8)
X_pca = pca.fit(X_sc).transform(X_sc)
#print(X_pca)
print("Before: {}".format(str(X_sc.shape)))
print("After: {}".format(str(X_pca.shape)))
print('sum of explained variance ratio: {0}'.format(sum(pca.explained_variance_ratio_)))

df = pd.DataFrame(X_pca)
df = df.add_prefix('RDKit_')
print(df)
df.to_csv('data/RDKit.csv', index=False)

