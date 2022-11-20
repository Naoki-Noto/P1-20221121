#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 19:46:05 2021

@author: notonaoki
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import mglearn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_samples
from matplotlib import cm

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

cluster_labels=np.unique(X_pred)
n_clusters=cluster_labels.shape[0]

# Silhouette coefficient
silhouette_vals=silhouette_samples(X_pca,X_pred,metric='euclidean')
y_ax_lower,y_ax_upper=0,0
yticks=[]

for i,c in enumerate(cluster_labels):
  c_silhouette_vals=silhouette_vals[X_pred==c]
  print(len(c_silhouette_vals))
  c_silhouette_vals.sort()
  y_ax_upper +=len(c_silhouette_vals)
  color=cm.jet(float(i)/n_clusters)
  plt.barh(range(y_ax_lower,y_ax_upper),
           c_silhouette_vals,
           height=1.0,
           edgecolor='none',
           color=color)
  yticks.append((y_ax_lower+y_ax_upper)/2.)
  y_ax_lower += len(c_silhouette_vals)

silhouette_avg=np.mean(silhouette_vals)
plt.axvline(silhouette_avg,color="red",linestyle="--")
plt.ylabel("Cluster", fontsize=16)
plt.xlabel("Silhouette coefficient", fontsize=16)
plt.tick_params(labelsize=16)
plt.show()

print(silhouette_avg)
#print(silhouette_vals)

# hybrid descriptors
fig.savefig("result_silhouette/hybrid/K-Means_{}.png".format(k))
ASC = pd.DataFrame(data=[silhouette_avg])
ASC.to_csv("result_silhouette/hybrid/asc_{}.csv".format(k))

# DFT descriptors
"""fig.savefig("result_silhouette/DFT/K-Means_{}.png".format(k))
ASC = pd.DataFrame(data=[silhouette_avg])
ASC.to_csv("result_silhouette/DFT/asc_{}.csv".format(k))"""

