import pandas as pd
from django.core.management import BaseCommand
from ourdatabase.models import Humankinase, ChemblIdLookup, Assays, Activities, TargetDictionary,CompoundStructures

#class Command(BaseCommand):
#    help = 'load a human kinase csv file into the database'
#
#    def add_arguments(self, parser):
#        parser.add_argument('--path',type=str)
#    
#    def handle(self, *args, **kwargs):
#        path = kwargs['path']
#        xxx = pd.read_excel(path)
#        xx = xxx.columns.values
#        for n in range(0,len(xxx)):
#                Humankinase.objects.create(
#                    kinase_id = n,
#                    x_name = xxx[xx[0]][n],
#                    manning_name = xxx[xx[1]][n],
#                    hgnc_name = xxx[xx[2]][n],
#                    kinase_name = xxx[xx[3]][n],
#                    group_name = xxx[xx[4]][n],
#                    family_name = xxx[xx[5]][n],
#                    subfamily_name = xxx[xx[6]][n], 
#                    uniprotid = xxx[xx[7]][n],
#                    chemblid = ChemblIdLookup.objects.get(chembl_id=xxx[xx[8]][n])
#                )
class Command(BaseCommand):
    kinase_id=1
    Humankinase_dic = Humankinase.objects.get(pk=kinase_id)
    target_chembl = Humankinase.objects.get(pk=kinase_id).chemblid
    target_dic = TargetDictionary.objects.get(chembl=target_chembl)
    assay_dic = Assays.objects.filter(tid=target_dic,assay_type__assay_type='B')
    Activities_dic = Activities.objects.filter(assay__in=assay_dic,pchembl_value__gte=5)
    table_val = []
    for activity in Activities_dic:
        target_name = Humankinase_dic.kinase_name
        target_id = activity.assay.tid.chembl.chembl_id
        compound_id = activity.molregno.chembl.chembl_id
        compound_smile = CompoundStructures.objects.get(molregno=activity.molregno).canonical_smiles
        assay_type = activity.assay.assay_type.assay_type
        pvalue = activity.pchembl_value
        x = {'target_name':target_name,'target_id':target_id,'compound_id':compound_id,'compound_smile': compound_smile, 'assay_type':assay_type,'pvalue':pvalue}
        table_val.append(x) 

    print(len(table_val))