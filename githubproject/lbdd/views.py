from django.shortcuts import render
from django.http import Http404, HttpResponse, StreamingHttpResponse
from rdkit import Chem
from rdkit.Chem import PandasTools, AllChem
import pandas as pd
import os,subprocess
import time
import logging

from web_v1.settings import JXYTEMPDIR, AMESDIR, MEDIA_ROOT, AMESDIR_DIR, HOBDIR
from .conformation_gen import d3confgen
from .hobpre import hobmodel_predict
from .forms import AmesForm, ConfGenForm, MolFilterForm
from .models import PropertyDocument,FilterDocument
from .mfilter import standardize

def molfilter(request):
    if request.method == 'POST':
        form = MolFilterForm(request.POST,request.FILES)
        if form.is_valid():
            fname = request.FILES['docfile']
            current_time = time.strftime("%Y%m%d-%H%M%S")
            tempfilename = JXYTEMPDIR + request.user.username + current_time +'.bak'
            with open(tempfilename,'wb+') as destination:
                for chunk in fname.chunks():
                    destination.write(chunk)
            df = pd.read_csv(tempfilename,header=None,usecols=[0],sep='\t')
            smiles_list = []
            for i in range(len(df)):
                smi = df.iloc[i][0]
                if not pd.isnull(smi):
                    smiles_list.append(smi)
            logger = logging.getLogger("django")
            logger.info(len(smiles_list))

            exportfile_x,errorfile_x = standardize(request.user.username,smiles_list)             
            newfile = FilterDocument(passed_file=exportfile_x,error_file=errorfile_x)
            newfile.save()
            dfile = FilterDocument.objects.get(passed_file=exportfile_x,error_file=errorfile_x)
            return render(request,'lbdd/mfilter.html',{'form':form, 'dfile':dfile})

    else:
        form = MolFilterForm()
        return render(request,'lbdd/mfilter.html',{'form':form,'dfile':[]}) 


def amespred(request):
    if request.method == 'POST':
        form = AmesForm(request.POST,request.FILES)
        smiles = []
        if form.is_valid():
            textaaa = form.cleaned_data['compounds']
            if textaaa:
                testaaa_list = textaaa.split()
                for smi in testaaa_list:
                    smiles.append(smi)
            else:
                logger = logging.getLogger("django")
                logger.info("no input in textarea")
            if not request.FILES:
                logger = logging.getLogger("django")
                logger.info("no file given")
            else:
                fname = request.FILES['docfile']
                current_time =  time.strftime("%Y%m%d-%H%M%S")
                tempfilename = JXYTEMPDIR + request.user.username + current_time +'.bak'
                with open(tempfilename,'wb+') as destination:
                    for chunk in fname.chunks():
                        destination.write(chunk)
                
                df = pd.read_csv(tempfilename)
                label_name = df.columns[0]
                logger = logging.getLogger("django")
                logger.info(os.getcwd())
                logger.info(AMESDIR)
                for index,smi in df.iterrows():
                    logger.info(smi[label_name])
                    smiles.append(smi[label_name])

        df_hob = hobmodel_predict(smiles,HOBDIR)
        logger.info(df_hob)

        df_predict = pd.DataFrame({'SMILES':smiles})
        current_time =  time.strftime("%Y%m%d-%H%M%S")
        tempfilename_input   = JXYTEMPDIR + request.user.username + current_time +'.input'
        tempfilename         = 'ames_results/' + request.user.username + current_time +'.csv'
        tempfilename_output  = JXYTEMPDIR + request.user.username + current_time +'.output'
        tempfilename_results = os.path.join(MEDIA_ROOT,tempfilename) 
        df_predict.to_csv(tempfilename_input,index=False)
        subprocess.run(["chemprop_predict","--test_path",tempfilename_input,"--checkpoint_dir",AMESDIR,"--preds_path",tempfilename_output]) 

        ames_results = pd.read_csv(tempfilename_output)
        ames_results.insert(2,'hob',df_hob[:,1].tolist())
        ames_results_sort = ames_results.sort_values('Label')
        PandasTools.AddMoleculeColumnToFrame(ames_results_sort,'SMILES','Molecule')
        PandasTools.SaveXlsxFromFrame(ames_results_sort,tempfilename_results,molCol='Molecule')

        ames_results_dic = ames_results.to_dict('records')
        #contend={'ames_results':ames_results}
        #for lig in ames_results_dic:
        #    logger.info(lig.get("SMILES"))
        newdoc = PropertyDocument(docfile = tempfilename)
        newdoc.save()
        dfile = PropertyDocument.objects.get(docfile=tempfilename)
        #return HttpResponse('Hello Mr.Jia')
        return render(request,'lbdd/property.html',{'form':form,'ames_results_dic':ames_results_dic,'dfile':dfile})
    else:
        form = AmesForm()
        #content={}
        return render(request,'lbdd/property.html',{'form':form,'ames_results':[],'dfile':[]})
    #return HttpResponse('Hello Mr.Jia')

# Create your views here.
def d3gen(request):
    if request.method == 'POST':
        form = ConfGenForm(request.POST,request.FILES)
        if form.is_valid():
            chi_type  = form.cleaned_data['chirality_source']
            conf_type = form.cleaned_data['conf_type'] 

            fname = request.FILES['docfile']
            current_time =  time.strftime("%Y%m%d-%H%M%S")
            tempfilename = JXYTEMPDIR + request.user.username + current_time +'.bak'
            with open(tempfilename,'wb+') as destination:
                for chunk in fname.chunks():
                    destination.write(chunk)

            mols = Chem.SDMolSupplier(tempfilename)
            exportfile,exportfile_x = d3confgen(request.user.username,mols,chi_type,conf_type)

            try:
                response = StreamingHttpResponse(open(exportfile,'rb'))
                response['content_type'] = "application/octet-stream"
                response['Content-Disposition'] = 'attachment; filename=' + exportfile_x
                return response
            except Exception:
                return Http404

    else:
        form = ConfGenForm()
        return render(request,'lbdd/d3gen.html',{'form':form})

def strtest(request,strcha):
    return HttpResponse(strcha)