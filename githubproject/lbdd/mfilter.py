import pandas as pd
import numpy as np
import rdkit as rk
import time,os
from rdkit import Chem
from rdkit.Chem import AllChem,Draw
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem.MolStandardize import rdMolStandardize
from rdkit.Chem.rdMolDescriptors import CalcNumHeteroatoms
from web_v1.settings import JXYTEMPDIR, MEDIA_ROOT

def std_mol(m):
    #m=Chem.MolFromSmiles(smi)
    clean_mol = rdMolStandardize.Cleanup(m)
    parent_clean_mol = rdMolStandardize.FragmentParent(clean_mol)
    uncharger = rdMolStandardize.Uncharger()
    uncharged_parent_clean_mol = uncharger.uncharge(parent_clean_mol)
    #te = rdMolStandardize.TautomerEnumerator()
    #taut_uncharged_parent_clean_mol = te.Canonicalize(uncharged_parent_clean_mol)

    #return taut_uncharged_parent_clean_mol
    return uncharged_parent_clean_mol

def standardize(user_name,smiles_list):

    allmols = []
    invalid_smi=[]

    for i in range(0,len(smiles_list)):
        try:
            mol = Chem.MolFromSmiles(smiles_list[i])
            allmols.append(std_mol(mol))
        except:
            invalid_smi.append(smiles_list[i])

    current_time = time.strftime("%Y%m%d-%H%M%S")
    correct_x = 'filter_results/' + user_name + current_time + '.sdf'
    correctfile = os.path.join(MEDIA_ROOT,correct_x) 
    error_x = 'filter_results/' + user_name + current_time + '.smi'
    errorfile = os.path.join(MEDIA_ROOT,error_x)

    w = Chem.SDWriter(correctfile)
    for mymol in allmols:
        w.write(mymol)
    w.close()


    if len(invalid_smi) > 0:
        with open(errorfile,'w') as f:
            for line in invalid_smi:
                f.write(f"{line}\n")
        f.close()
    else:
        with open(errorfile,'w') as f:
            f.write("all passed")
        f.close()

    return correct_x,error_x