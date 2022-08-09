from rdkit import Chem
from rdkit.Chem import rdDistGeom
from rdkit.Chem import AllChem
import time
from rdkit.Chem import rdMolAlign
from rdkit.Chem.EnumerateStereoisomers import EnumerateStereoisomers, StereoEnumerationOptions
import logging

from web_v1.settings import JXYTEMPDIR

def d3confgen(user_name,mols,chitype,conftype):
    #mols = Chem.SDMolSupplier(inputfile)
    ms = [Chem.AddHs(m) for m in mols]
    #m = ms[0]

    #ChiralCenters=[] 
    current_time = time.strftime("%Y%m%d-%H%M%S")
    writefile = JXYTEMPDIR + user_name + current_time + '.sdf'
    filename_x = user_name + current_time + '.sdf'
    w = Chem.SDWriter(writefile)
    
    nmol = 0
    logger = logging.getLogger("django")
    for m in ms:
        nmol = nmol +1
        if chitype == 'Enumerate':
            opts = StereoEnumerationOptions(tryEmbedding=True) 
            isomers = tuple(EnumerateStereoisomers(m,options=opts))
        elif chitype == 'Keep':
            if conftype == '3D':
                Chem.AssignAtomChiralTagsFromStructure(m)
            isomers=[m]

        nnn = 0
        for onemol in isomers:
            nnn = nnn + 1
            ps = AllChem.ETKDGv3()
            ps.randomSeed=0xf00d
            ps.pruneRmsThresh = 0.5
            #ChiralCenters.append(Chem.FindMolChiralCenters(onemol))
            cids = AllChem.EmbedMultipleConfs(onemol,50,ps)

            mp = AllChem.MMFFGetMoleculeProperties(onemol, mmffVariant='MMFF94s')
            AllChem.MMFFOptimizeMoleculeConfs(onemol,numThreads=0,mmffVariant='MMFF94s')

            res=[]
            for cid in cids:
                ff = AllChem.MMFFGetMoleculeForceField(onemol,mp,confId=cid)
                e = ff.CalcEnergy()
                res.append((cid,e))

                sorted_res = sorted(res,key=lambda x:x[1])
                rdMolAlign.AlignMolConformers(onemol)
            ### modify code for similarity ###
            #njxy = 0
            for cid, e in sorted_res:
                onemol.SetProp('mol_id',str(nmol))
                onemol.SetProp('isomer_id',str(nnn))
                onemol.SetProp('CID',str(cid))
                onemol.SetProp('Energy',str(e))
                w.write(onemol,confId=cid)
                #njxy = njxy +1
                #if njxy == 1:
                #    break

            logger.info(nmol)


    w.close()
    return writefile, filename_x