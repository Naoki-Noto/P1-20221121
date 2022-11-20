#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 01:34:26 2021

@author: notonaoki
"""

import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors

def calculate_descriptors(mols, names=None):
    if names is None:
        names = [d[0] for d in Descriptors._descList]
    calc = MoleculeDescriptors.MolecularDescriptorCalculator(names)
    descs = [calc.CalcDescriptors(mol) for mol in mols]
    descs = pd.DataFrame(descs, columns=names)
    return descs

suppl = Chem.SDMolSupplier('SDF/3a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df1 = calculate_descriptors(mols_from_sm)
print(df1)

suppl = Chem.SDMolSupplier('SDF/3b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df2 = calculate_descriptors(mols_from_sm)
print(df2)

suppl = Chem.SDMolSupplier('SDF/3c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df3 = calculate_descriptors(mols_from_sm)
print(df3)

suppl = Chem.SDMolSupplier('SDF/3d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df4 = calculate_descriptors(mols_from_sm)
print(df4)

suppl = Chem.SDMolSupplier('SDF/3e.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df5 = calculate_descriptors(mols_from_sm)
print(df5)

suppl = Chem.SDMolSupplier('SDF/3f.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df6 = calculate_descriptors(mols_from_sm)
print(df6)

suppl = Chem.SDMolSupplier('SDF/3g.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df7 = calculate_descriptors(mols_from_sm)
print(df7)

suppl = Chem.SDMolSupplier('SDF/3h.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df8 = calculate_descriptors(mols_from_sm)
print(df8)

suppl = Chem.SDMolSupplier('SDF/3i.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df9 = calculate_descriptors(mols_from_sm)
print(df9)

suppl = Chem.SDMolSupplier('SDF/3j.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df10 = calculate_descriptors(mols_from_sm)
print(df10)

suppl = Chem.SDMolSupplier('SDF/3k.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df11 = calculate_descriptors(mols_from_sm)
print(df11)

suppl = Chem.SDMolSupplier('SDF/3l.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df12 = calculate_descriptors(mols_from_sm)
print(df12)

suppl = Chem.SDMolSupplier('SDF/4a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df13 = calculate_descriptors(mols_from_sm)
print(df13)

suppl = Chem.SDMolSupplier('SDF/4b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df14 = calculate_descriptors(mols_from_sm)
print(df14)

suppl = Chem.SDMolSupplier('SDF/4c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df15 = calculate_descriptors(mols_from_sm)
print(df15)

suppl = Chem.SDMolSupplier('SDF/5a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df16 = calculate_descriptors(mols_from_sm)
print(df16)

suppl = Chem.SDMolSupplier('SDF/5b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df17 = calculate_descriptors(mols_from_sm)
print(df17)

suppl = Chem.SDMolSupplier('SDF/6a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df18 = calculate_descriptors(mols_from_sm)
print(df18)

suppl = Chem.SDMolSupplier('SDF/6b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df19 = calculate_descriptors(mols_from_sm)
print(df19)

suppl = Chem.SDMolSupplier('SDF/7a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df20 = calculate_descriptors(mols_from_sm)
print(df20)

suppl = Chem.SDMolSupplier('SDF/7b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df21 = calculate_descriptors(mols_from_sm)
print(df21)

suppl = Chem.SDMolSupplier('SDF/7c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df22 = calculate_descriptors(mols_from_sm)
print(df22)

suppl = Chem.SDMolSupplier('SDF/7d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df23 = calculate_descriptors(mols_from_sm)
print(df23)

suppl = Chem.SDMolSupplier('SDF/7e.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df24 = calculate_descriptors(mols_from_sm)
print(df24)

suppl = Chem.SDMolSupplier('SDF/7f.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df25 = calculate_descriptors(mols_from_sm)
print(df25)

suppl = Chem.SDMolSupplier('SDF/7g.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df26 = calculate_descriptors(mols_from_sm)
print(df26)

suppl = Chem.SDMolSupplier('SDF/7h.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df27 = calculate_descriptors(mols_from_sm)
print(df27)

suppl = Chem.SDMolSupplier('SDF/7i.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df28 = calculate_descriptors(mols_from_sm)
print(df28)

suppl = Chem.SDMolSupplier('SDF/8a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df29 = calculate_descriptors(mols_from_sm)
print(df29)

suppl = Chem.SDMolSupplier('SDF/8b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df30 = calculate_descriptors(mols_from_sm)
print(df30)

suppl = Chem.SDMolSupplier('SDF/8c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df31 = calculate_descriptors(mols_from_sm)
print(df31)

suppl = Chem.SDMolSupplier('SDF/8d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df32 = calculate_descriptors(mols_from_sm)
print(df32)

suppl = Chem.SDMolSupplier('SDF/8e.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df33 = calculate_descriptors(mols_from_sm)
print(df33)

suppl = Chem.SDMolSupplier('SDF/8f.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df34 = calculate_descriptors(mols_from_sm)
print(df34)

suppl = Chem.SDMolSupplier('SDF/8g.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df35 = calculate_descriptors(mols_from_sm)
print(df35)

suppl = Chem.SDMolSupplier('SDF/9a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df36 = calculate_descriptors(mols_from_sm)
print(df36)

suppl = Chem.SDMolSupplier('SDF/9b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df37 = calculate_descriptors(mols_from_sm)
print(df37)

suppl = Chem.SDMolSupplier('SDF/9c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df38 = calculate_descriptors(mols_from_sm)
print(df38)

suppl = Chem.SDMolSupplier('SDF/10a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df39 = calculate_descriptors(mols_from_sm)
print(df39)

suppl = Chem.SDMolSupplier('SDF/10b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df40 = calculate_descriptors(mols_from_sm)
print(df40)

suppl = Chem.SDMolSupplier('SDF/10c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df41 = calculate_descriptors(mols_from_sm)
print(df41)

suppl = Chem.SDMolSupplier('SDF/10d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df42 = calculate_descriptors(mols_from_sm)
print(df42)

suppl = Chem.SDMolSupplier('SDF/10e.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df43 = calculate_descriptors(mols_from_sm)
print(df43)

suppl = Chem.SDMolSupplier('SDF/11a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df44 = calculate_descriptors(mols_from_sm)
print(df44)

suppl = Chem.SDMolSupplier('SDF/11b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df45 = calculate_descriptors(mols_from_sm)
print(df45)

suppl = Chem.SDMolSupplier('SDF/11c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df46 = calculate_descriptors(mols_from_sm)
print(df46)

suppl = Chem.SDMolSupplier('SDF/12a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df47 = calculate_descriptors(mols_from_sm)
print(df47)

suppl = Chem.SDMolSupplier('SDF/12b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df48 = calculate_descriptors(mols_from_sm)
print(df48)

suppl = Chem.SDMolSupplier('SDF/12c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df49 = calculate_descriptors(mols_from_sm)
print(df49)

suppl = Chem.SDMolSupplier('SDF/12d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df50 = calculate_descriptors(mols_from_sm)
print(df50)

suppl = Chem.SDMolSupplier('SDF/13a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df51 = calculate_descriptors(mols_from_sm)
print(df51)

suppl = Chem.SDMolSupplier('SDF/13b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df52 = calculate_descriptors(mols_from_sm)
print(df52)

suppl = Chem.SDMolSupplier('SDF/13c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df53 = calculate_descriptors(mols_from_sm)
print(df53)

suppl = Chem.SDMolSupplier('SDF/13d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df54 = calculate_descriptors(mols_from_sm)
print(df54)

suppl = Chem.SDMolSupplier('SDF/14a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df55 = calculate_descriptors(mols_from_sm)
print(df55)

suppl = Chem.SDMolSupplier('SDF/14b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df56 = calculate_descriptors(mols_from_sm)
print(df56)

suppl = Chem.SDMolSupplier('SDF/15.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df57 = calculate_descriptors(mols_from_sm)
print(df57)

suppl = Chem.SDMolSupplier('SDF/16.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df58 = calculate_descriptors(mols_from_sm)
print(df58)

suppl = Chem.SDMolSupplier('SDF/17.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df59 = calculate_descriptors(mols_from_sm)
print(df59)

suppl = Chem.SDMolSupplier('SDF/18.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
df60 = calculate_descriptors(mols_from_sm)
print(df60)


df_sum = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10,
                    df11, df12, df13, df14, df15, df16, df17, df18, df19, df20,
                    df21, df22, df23, df24, df25, df26, df27, df28, df29, df30,
                    df31, df32, df33, df34, df35, df36, df37, df38, df39, df40,
                    df41, df42, df43, df44, df45, df46, df47, df48, df49, df50,
                    df51, df52, df53, df54, df55, df56, df57, df58, df59, df60])

print(df_sum)
df_sum.to_csv("data/MoleculeDescriptors.csv", index=False)


