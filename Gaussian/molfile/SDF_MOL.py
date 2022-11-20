#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 15:00:42 2021

@author: notonaoki
"""

from rdkit import Chem
from rdkit.Chem import AllChem

suppl = Chem.SDMolSupplier('SDF/3a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
def ETKDG(mols, version=1):
    mhs = [Chem.AddHs(mol) for mol in mols]
    for mol in mhs:
        if version == 1:
            p = AllChem.ETKDG()
        elif version == 2:
            p = AllChem.ETKDGv2()
        elif version == 3:
            p = AllChem.ETKDGv3()
        else:
            print('invalid input')
        AllChem.EmbedMolecule(mol, p)
    return mol
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3a.mol')

suppl = Chem.SDMolSupplier('SDF/3b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3b.mol')

suppl = Chem.SDMolSupplier('SDF/3c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3c.mol')

suppl = Chem.SDMolSupplier('SDF/3d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3d.mol')

suppl = Chem.SDMolSupplier('SDF/3e.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3e.mol')

suppl = Chem.SDMolSupplier('SDF/3f.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3f.mol')

suppl = Chem.SDMolSupplier('SDF/3g.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3g.mol')

suppl = Chem.SDMolSupplier('SDF/3h.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3h.mol')

suppl = Chem.SDMolSupplier('SDF/3i.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3i.mol')

suppl = Chem.SDMolSupplier('SDF/3j.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3j.mol')

suppl = Chem.SDMolSupplier('SDF/3k.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3k.mol')

suppl = Chem.SDMolSupplier('SDF/3l.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/3l.mol')

suppl = Chem.SDMolSupplier('SDF/4a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/4a.mol')

suppl = Chem.SDMolSupplier('SDF/4b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/4b.mol')

suppl = Chem.SDMolSupplier('SDF/4c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/4c.mol')

suppl = Chem.SDMolSupplier('SDF/5a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/5a.mol')

suppl = Chem.SDMolSupplier('SDF/5b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/5b.mol')

suppl = Chem.SDMolSupplier('SDF/6a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/6a.mol')

suppl = Chem.SDMolSupplier('SDF/6b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/6b.mol')

suppl = Chem.SDMolSupplier('SDF/7a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/7a.mol')

suppl = Chem.SDMolSupplier('SDF/7b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/7b.mol')

suppl = Chem.SDMolSupplier('SDF/7c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/7c.mol')

suppl = Chem.SDMolSupplier('SDF/7d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/7d.mol')

suppl = Chem.SDMolSupplier('SDF/7e.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/7e.mol')

suppl = Chem.SDMolSupplier('SDF/7f.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/7f.mol')

suppl = Chem.SDMolSupplier('SDF/7g.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/7g.mol')

suppl = Chem.SDMolSupplier('SDF/7h.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/7h.mol')

suppl = Chem.SDMolSupplier('SDF/7i.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/7i.mol')

suppl = Chem.SDMolSupplier('SDF/8a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/8a.mol')

suppl = Chem.SDMolSupplier('SDF/8b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/8b.mol')

suppl = Chem.SDMolSupplier('SDF/8c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/8c.mol')

suppl = Chem.SDMolSupplier('SDF/8d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/8d.mol')

suppl = Chem.SDMolSupplier('SDF/8e.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/8e.mol')

suppl = Chem.SDMolSupplier('SDF/8f.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/8f.mol')

suppl = Chem.SDMolSupplier('SDF/8g.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/8g.mol')

suppl = Chem.SDMolSupplier('SDF/9a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/9a.mol')

suppl = Chem.SDMolSupplier('SDF/9b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/9b.mol')

suppl = Chem.SDMolSupplier('SDF/9c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/9c.mol')

suppl = Chem.SDMolSupplier('SDF/10a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/10a.mol')

suppl = Chem.SDMolSupplier('SDF/10b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/10b.mol')

suppl = Chem.SDMolSupplier('SDF/10c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/10c.mol')

suppl = Chem.SDMolSupplier('SDF/10d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/10d.mol')

suppl = Chem.SDMolSupplier('SDF/10e.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/10e.mol')

suppl = Chem.SDMolSupplier('SDF/11a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/11a.mol')

suppl = Chem.SDMolSupplier('SDF/11b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/11b.mol')

suppl = Chem.SDMolSupplier('SDF/11c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/11c.mol')

suppl = Chem.SDMolSupplier('SDF/12a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/12a.mol')

suppl = Chem.SDMolSupplier('SDF/12b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/12b.mol')

suppl = Chem.SDMolSupplier('SDF/12c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/12c.mol')

suppl = Chem.SDMolSupplier('SDF/12d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/12d.mol')

suppl = Chem.SDMolSupplier('SDF/13a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/13a.mol')

suppl = Chem.SDMolSupplier('SDF/13b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/13b.mol')

suppl = Chem.SDMolSupplier('SDF/13c.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/13c.mol')

suppl = Chem.SDMolSupplier('SDF/13d.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/13d.mol')

suppl = Chem.SDMolSupplier('SDF/14a.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/14a.mol')

suppl = Chem.SDMolSupplier('SDF/14b.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/14b.mol')

suppl = Chem.SDMolSupplier('SDF/15.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/15.mol')

suppl = Chem.SDMolSupplier('SDF/16.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/16.mol')

suppl = Chem.SDMolSupplier('SDF/17.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/17.mol')

suppl = Chem.SDMolSupplier('SDF/18.sdf', removeHs=False)
mols = [x for x in suppl if x is not None]
print('Number of input molecules:',len(mols))
smiles = [Chem.MolToSmiles(mol) for mol in mols]
mols_from_sm = [Chem.MolFromSmiles(sm) for sm in smiles]
ETKDG_m = ETKDG(mols_from_sm, 3)
Chem.MolToMolFile(ETKDG_m, 'MOL/18.mol')

