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


DFT = pd.read_csv('data/DFT.csv')
RDKit = pd.read_csv('data/RDKit.csv')
yield_class = pd.read_csv('data/yield_class.csv')

name = yield_class.drop(columns=['Yield_2h','Yield_12h','Class'])
DFT = DFT.drop(columns=['Name','id'])
yc = yield_class.drop(columns=['Name','id'])

data_h = pd.concat([name, DFT, RDKit, yc], axis=1, join='inner')
data_R = pd.concat([name, RDKit, yc], axis=1, join='inner')
data_D = pd.concat([name, DFT, yc], axis=1, join='inner')
print(data_h)
print(data_R)
print(data_D)

data_h.to_csv('data/data_hybrid_descriptors.csv', index=False)
data_R.to_csv('data/data_RDKit_descriptors.csv', index=False)
data_D.to_csv('data/data_DFT_descriptors.csv', index=False)

