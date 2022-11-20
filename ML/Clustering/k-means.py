#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 19:46:05 2021

@author: notonaoki
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
import mglearn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

k=5

data = pd.read_csv('data.csv')
X = data.drop(columns=['Name', 'id', 'Yield_2h', 'Yield_12h', 'Class',
                       #'RDKit_0', 'RDKit_1', 'RDKit_2', 'RDKit_3','RDKit_4', 'RDKit_5','RDKit_6', 'RDKit_7',
                       ])
#print(X)

sc = StandardScaler()
X_sc = sc.fit(X).transform(X)
#print(X_sc)

pca = PCA(n_components=2)
X_pca = pca.fit(X_sc).transform(X_sc)
#print(X_pca)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
kmeans = KMeans(n_clusters=k, random_state=0)
X_pred = kmeans.fit(X_pca).predict(X_pca)
#print(X_pred)
mglearn.discrete_scatter(X_pca[:, 0], X_pca[:, 1], kmeans.labels_, markers='o')
plt.xlim(-4,5)
plt.ylim(-4,5)
ax.set_aspect('equal', adjustable='box')
plt.xlabel("First principal component", fontsize=16)
plt.ylabel("Second principal component", fontsize=16)
plt.tick_params(labelsize=16)
#mglearn.discrete_scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],[0, 1, 2, 3, 4], markers='^', markeredgewidth=2)
plt.show()

# hybrid descriptors
fig.savefig("result_k-means/hybrid/k-means_{}.png".format(k))

# DFT descriptors
"""fig.savefig("result_k-means/DFT/k-means_{}.png".format(k))"""

