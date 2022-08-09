from ast import Continue
from django.forms.formsets import formset_factory
from django.http import Http404, StreamingHttpResponse
from django.http.response import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from web_v1.settings import JXYTEMPDIR

from ourdatabase.models import CompoundStructures,Humankinase,TargetDictionary,Assays,Activities,MoleculeDictionary,ChemblIdLookup,Osrimolecule
from .models import Document, thankspic,wntmolecule
from .forms import AdvancedSearchForm, ContactForm, MolSmile, OsriMoleculeForm, DocumentForm, TestForm
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors
import logging
from chembl_webresource_client.new_client import new_client
from django.conf import settings
import os
import time
from django.contrib.auth.decorators import login_required
import random
from django.forms import formset_factory
from datetime import datetime
import pandas as pd

# Create your views here.

@login_required
def as_inhouse(request):
    form  = AdvancedSearchForm(request.POST)
    asdic = {}
    if form.is_valid():

        asdic['ligand_id']  = form.cleaned_data['AS_ligand_id']
        asdic['target_id']  = form.cleaned_data['AS_target_id']
        asdic['assay_type'] = form.cleaned_data['AS_assay_type']
        asdic['recorder']   = form.cleaned_data['AS_recorder']

        logger = logging.getLogger("django")
        logger.info(asdic)

        allosrimolecule = Osrimolecule.objects.all()

        for k,v in asdic.items():
            if not v:
                logger.info(k+'is blank')
            else:
                allosrimolecule = allosrimolecule.filter(**{k:v})

    testformset = formset_factory(TestForm,extra=len(allosrimolecule))
    formset = testformset()

    alltogether = zip(allosrimolecule,formset)
    for compound,form in alltogether:
        form.initial['fname'] = compound.ligand_id

    logger.info(len(allosrimolecule))
    logger.info(len(formset))
    content = {'allosrimolecule':allosrimolecule,'formset':formset}
    return render(request,'chemblbase/inhouse.html',content)
    #content = {'allosrimolecule':allosrimolecule}
    #return render(request,'chemblbase/inhouse.html',content)    
#return HttpResponse('hello world')

@login_required
def delmol(request): 
    if request.POST.get('delete_id'):
        logger = logging.getLogger("django")
        logger.info('delete')
        logger.info(request.POST.get('delete_id'))
        deletemol = Osrimolecule.objects.get(ligand_id=request.POST.get('delete_id'))
        deletemol.delete()
        return HttpResponseRedirect(reverse('chemblbase:inhousecompound'))

@login_required
def editmol(request):
    if request.POST.get('edit_id'):
        logger = logging.getLogger("django")
        logger.info('edit')
        logger.info(request.POST.get('edit_id'))
        emol = Osrimolecule.objects.get(ligand_id=request.POST.get('edit_id'))
        form = OsriMoleculeForm(initial={'ligand_id':emol.ligand_id,\
            'ligand':emol.canonical_smiles,'target':emol.target_id,'assay_type':emol.assay_type,\
            'activity_type':emol.activity_type,'activity_value':emol.activity_value,\
            'activity_unit':emol.activity_unit,'disease':emol.disease,'descriptions':emol.descriptions})
        #form.ligand_id = emol.ligand_id
        #form.ligand = emol.canonical_smiles 
        #form.target = emol.target_id
        #form.assay_type = emol.assay_type
        #form.activity_type = emol.activity_type
        #form.activity_value = emol.activity_value
        #form.activity_unit = emol.activity_unit
        return render(request,'chemblbase/getmol.html',{'form':form})

@login_required
def showinhouse(request):
    logger = logging.getLogger("django") 
    allosrimolecule = Osrimolecule.objects.all()
    if request.method == 'POST':
        form  = AdvancedSearchForm(request.POST)
        asdic = {}
        if form.is_valid():

            asdic['ligand_id']  = form.cleaned_data['AS_ligand_id']
            asdic['target_id']  = form.cleaned_data['AS_target_id']
            asdic['assay_type'] = form.cleaned_data['AS_assay_type']
            asdic['recorder']   = form.cleaned_data['AS_recorder']

            logger.info(asdic)

            #allosrimolecule = Osrimolecule.objects.all()

            for k,v in asdic.items():
                if not v:
                    logger.info(k+'is blank')
                else:
                    allosrimolecule = allosrimolecule.filter(**{k:v})

    #allosrimolecule = Osrimolecule.objects.all()
    #form = AdvancedSearchForm()
### edit 
    #if request.POST.get('delete_id'):
    #    logger = logging.getLogger("django")
    #    logger.info('delete')
    #    logger.info(request.POST.get('delete_id'))
    #    deletemol = Osrimolecule.objects.filter(ligand_id=request.POST.get('delete_id'))
    #    deletemol.delete()
    #    return HttpResponseRedirect(reverse('chemblbase:inhousecompound'))
    
    #if request.POST.get('edit_id'):
    #    logger = logging.getLogger("django")
    #    logger.info('edit')
    #    logger.info(request.POST.get('edit_id'))
    #    return HttpResponseRedirect(reverse('chemblbase:inhousecompound'))

###
    for compound in allosrimolecule:
        #compound.image = compound.image
        #compound.save()
        #if not compound.image:
        #    file_path = settings.STATICFILES_DIRS[0] + '\\images\inhouse'
        #    file_path_name = file_path + '\\' + compound.ligand_id + '.png'
        #    x = Chem.MolFromSmiles(compound.canonical_smiles)
        #    Draw.MolToFile(x,file_path_name)
        #    compound.image = file_path_name
        #    compound.save()
        #logger = logging.getLogger("django") 
        #logger.info(compound.img_temp)
        if not compound.img_temp: 
            file_path = settings.MEDIA_ROOT + '//images/inhouse'
            logger.info(file_path)
            file_path_name = file_path + '//' + compound.ligand_id + '.png' 
            logger.info(file_path_name)
            x = Chem.MolFromSmiles(compound.canonical_smiles)
            Draw.MolToFile(x,file_path_name)
            #filename = '\\images\inhouse' + compound.ligand_id + '.png'
            filename = '//images/inhouse' + '//' + compound.ligand_id + '.png'
            compound.img_temp = filename
            compound.save()

    testformset = formset_factory(TestForm,extra=len(allosrimolecule))
    formset = testformset()

    alltogether = zip(allosrimolecule,formset)
    for compound,form in alltogether:
        form.initial['fname'] = compound.ligand_id

    logger.info(len(allosrimolecule))
    logger.info(len(formset))
    content = {'allosrimolecule':allosrimolecule,'formset':formset}
    return render(request,'chemblbase/inhouse.html',content)

@login_required
def exportfile(request):
    testformset = formset_factory(TestForm)
    formset = testformset(request.POST)
    logger = logging.getLogger("django")
    logger.info(len(formset))
    logger.info(formset.cleaned_data)
    logger.info(request.POST.get('fileformat'))
    logger.info(request.POST.get('items'))
    cd = formset.cleaned_data
   
    usedlig = []
    for cd_one in cd:
        if cd_one:
            if request.POST.get('items') == 'All':
                usedlig.append(cd_one['fname'])
            elif request.POST.get('items') == 'Selected':
                if cd_one['slect']:
                    usedlig.append(cd_one['fname'])
    logger.info(usedlig)

    if request.POST.get('fileformat') == 'SDF':
        current_datetime = time.strftime("%Y%m%d-%H%M%S")
        filename = '/tmp/' + request.user.username + current_datetime + '.sdf'
        filename_x = request.user.username + current_datetime + '.sdf'
        logger.info(filename)
        with Chem.SDWriter(filename) as w:
            for ligand_id in usedlig:
                compound = Osrimolecule.objects.get(ligand_id=ligand_id)
                mol = Chem.MolFromSmiles(compound.canonical_smiles)
                if compound.activity_value:
                    mol.SetDoubleProp("Activity",float(compound.activity_value))
                #else:
                #    mol.SetDoubleProp("Activity",'None')
                #mol.SetDoubleProp("Activity",float(compound.activity_value))  
                w.write(mol)
        w.close()

    try:
        response = StreamingHttpResponse(open(filename,'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + filename_x
        return response
    except Exception:
        return Http404

 #   return HttpResponse('Fuck you')

@login_required
def jmewindow(request):
    return render(request,'chemblbase/jme_window.html',{})

@login_required
def chemblmainpage(request):
    return render(request,'chemblbase/mainpage.html',{})
 

@login_required
def singlemolecule(request,chemblid):
    chb = ChemblIdLookup.objects.get(chembl_id=chemblid)
    mol = MoleculeDictionary.objects.get(chembl=chb)
    try:
        compound_str = CompoundStructures.objects.get(molregno=mol)
        compound_smile = compound_str.canonical_smiles
    except compound_str.DoesNotExist:
        compound_smile = ''
    content={'compound_smile':compound_smile}
    return render(request,'chemblbase/singlemolecule.html',content) 

@login_required
def singlemoleculeosri(request,chemblid):
    mol = Osrimolecule.objects.get(ligand_id=chemblid)
    compound_smile = mol.canonical_smiles
    content={'compound_smile':compound_smile}
    return render(request,'chemblbase/singlemoleculeosri.html',content) 

@login_required
def compound(request):
    allcompounds = CompoundStructures.objects.all()[:100]
    content = {'allcompounds': allcompounds}
    return render(request,'chemblbase/compound.html',content)

@login_required
def index(request,kinase_id):
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
        try:
          compound_str = CompoundStructures.objects.get(molregno=activity.molregno)
          compound_smile = compound_str.canonical_smiles
        except compound_str.DoesNotExist:
          compound_smile = 'jxytest'
        assay_type = activity.assay.assay_type.assay_type
        pvalue = activity.pchembl_value
        x = {'target_name':target_name,'target_id':target_id,'compound_id':compound_id,'compound_smile': compound_smile, 'assay_type':assay_type,'pvalue':pvalue}
        table_val.append(x)
    #for i in range(0,len(Activities_dic)):
    #   compound_dic = CompoundStructures.objects.get(molregno=Activities_dic[i].molregno)

    content = {'table_val':table_val}

    return render(request,'chemblbase/index.html',content) 

@login_required
def allkinase(request):
    human_kinases = Humankinase.objects.all()
    content = {'human_kinases':human_kinases}
    return render(request,'chemblbase/humankinase.html',content)

@login_required
def get_contact(request):
    # 如果form通过POST方法发送数据
    if request.method == 'POST':
        # 接受request.POST参数构造form类的实例
        form = ContactForm(request.POST)
        # 验证数据是否合法
        if form.is_valid():
            # 处理form.cleaned_data中的数据
            # ...
            # 重定向到一个新的URL
            return HttpResponseRedirect('/thanks/')

    # 如果是通过GET方法请求数据，返回一个空的表单
    else:
        form = ContactForm()

    return render(request,'chemblbase/contact.html', {'form': form})

@login_required
def showthanks(request):
    index_num=random.randint(1,10)
    wntcompound = thankspic.objects.get(pk=index_num)
    return render(request,'chemblbase/thanks.html',{"wntcompound":wntcompound})

@login_required
def drawmolecule(request):
    return render(request,'chemblbase/drawmolecule.html',{})

def create_new_ref_number():
    not_unique = True
    while not_unique:
        unique_ref = random.randint(10000000, 99999999)
        if not Osrimolecule.objects.filter(ligand_id='CHN'+unique_ref):
         not_unique = False
    return str(unique_ref)

def create_new_ref_number2():
    for i in range(0,999999):
        unique_ref='PLG-'+str(i).zfill(7)
        if not Osrimolecule.objects.filter(ligand_id=unique_ref):
            break
    return unique_ref

@login_required
def get_mol(request):
    logger = logging.getLogger("django")
    logger.info("Whatever to log")

    if request.method == 'POST':
        form = OsriMoleculeForm(request.POST)
        if form.is_valid():
            logger.info("Whatever to log")
            #lig_id = form.cleaned_data['ligand_id']
            lig_smile = form.cleaned_data['ligand']
            tar_id = form.cleaned_data['target']
            ass_type = form.cleaned_data['assay_type']
            act_type = form.cleaned_data['activity_type']
            act_unit = form.cleaned_data['activity_unit']
            act_value = form.cleaned_data['activity_value']
            disease = form.cleaned_data['disease']
            descriptions = form.cleaned_data['descriptions']
            
            if not form.cleaned_data['ligand_id']:
                lig_id = create_new_ref_number2()
            else:
                lig_id = form.cleaned_data['ligand_id']
            logger.info("Whatever to log222")

            m = Chem.MolFromSmiles(lig_smile)
            logp_value = Descriptors.MolLogP(m)
            tpsa_value = Descriptors.TPSA(m)
            recorder_val = request.user.username
           
            #file_path = settings.STATICFILES_DIRS[0] + '//images/inhouse'
            #file_path_name = file_path + '//' + lig_id + '.png'
            ### 20220121
            #tttname = lig_id + '.png'
            ### end of 20220121
            #logger.info(file_path_name)
            #x = Chem.MolFromSmiles(lig_smile)
            #Draw.MolToFile(x,file_path_name)   

            
            #Osrimolecule.save()
            #q = Osrimolecule(ligand_id=lig_id,logp=logp_value,canonical_smiles=lig_smile,target_id=tar_id,assay_type=ass_type,activity_type=act_type,tpsa=tpsa_value,activity_unit=act_unit,activity_value=act_value,recorder=recorder_val,image=file_path_name,disease=disease,descriptions=descriptions)
            q = Osrimolecule(ligand_id=lig_id,logp=logp_value,canonical_smiles=lig_smile,target_id=tar_id,assay_type=ass_type,activity_type=act_type,tpsa=tpsa_value,activity_unit=act_unit,activity_value=act_value,recorder=recorder_val,disease=disease,descriptions=descriptions)

            q.save()
            return HttpResponseRedirect('thanks')  
    else:
        form = OsriMoleculeForm() 

    return render(request,'chemblbase/getmol.html',{'form':form})

@login_required
def ad_search(request):
    form = AdvancedSearchForm()
    return render(request,'chemblbase/adsearch.html',{'form':form})

@login_required
def substructure_search(request):
    if request.method == 'POST':
        form = MolSmile(request.POST)
        sub_smiles = form.cleaned_data['ligand_smile']
        res = new_client.substructure.filter(smiles=sub_smiles).only(['molecule_chembl_id','molecule_structures'])
        table_data=[]
        for res_id in res:
            activities = new_client.activity.filter(molecule_chembl_id=res_id['molecule_chembl_id'])
            for activity_id in activities:
                x={'molecule_id':res_id['molecule_chembl_id'],'molecule_smiles':res_id['molecule_structure']['canonical_smiles'],'assay_description':activity_id['assay_description'],'assay_type':activity_id['assay_type'],\
                  'target_id':activity_id['target_chembl_id'],'target_name':activity_id['target_pref_name'],'type':activity_id['standard_type'],'unit':activity_id['standard_units'],'value': activity_id['standard_value']}
                table_data=table_data.append(x)
        content={'table_data':table_data}

              

    else:
        form = MolSmile()
        return render(request,'chemblbase/substructure_smile.html',{'form':form}) 
  
@login_required
def substructure_search_results(request):
    logger = logging.getLogger("django")
    #timestr = time.strftime("%Y%m%d-%H%M%S")
    #file_name = settings.STATICFILES_DIRS[0] + '//' + timestr 
    #os.mkdir(file_name)
    #file_name = file_name + '//image'
    #os.mkdir(file_name)

    if request.method == 'POST':
        form = MolSmile(request.POST)
        if form.is_valid():
            sub_smiles = form.cleaned_data['ligand_smile']
            data_source = form.cleaned_data['datasource']
            if data_source == 'Chembl27':

                timestr = time.strftime("%Y%m%d-%H%M%S")
                file_name = settings.STATICFILES_DIRS[0] + '//' + timestr 
                os.mkdir(file_name)
                file_name = file_name + '//image'
                os.mkdir(file_name)

                res = new_client.substructure.filter(smiles=sub_smiles).only(['molecule_chembl_id','molecule_structures'])
                table_data=[]
                for res_id in res:
                ### generate images ###
                ### timestr = time.strftime("%Y%m%d-%H%M%S")
                ### file_name = settings.STATICFILES_DIRS[0] + '\\' + timestr 
                ### os.mkdir(file_name)
                ### file_name = file_name + '\\image' 
                ### os.mkdir(file_name)
                    file_name_current = file_name + '//' + res_id['molecule_chembl_id'] + '.png'
                    x = Chem.MolFromSmiles(res_id['molecule_structures']['canonical_smiles'])
                    Draw.MolToFile(x,file_name_current)
                    logger.info(file_name_current)
                    file_name_current = '//' + timestr + '//image//' + res_id['molecule_chembl_id'] + '.png'
                ### end of generation ###
                    activities = new_client.activity.filter(molecule_chembl_id=res_id['molecule_chembl_id']).only(['assay_description','assay_type','target_chembl_id','target_pref_name','standard_type','standard_units','standard_value'])
                    for activity_id in activities:
                        x={'molecule_id':res_id['molecule_chembl_id'],'image_url':file_name_current,'assay_description':activity_id['assay_description'],'assay_type':activity_id['assay_type'],\
                           'target_id':activity_id['target_chembl_id'],'target_name':activity_id['target_pref_name'],'type':activity_id['standard_type'],'unit':activity_id['standard_units'],'value': activity_id['standard_value']}
                        table_data.append(x)
                content={'table_data':table_data} 
                return render(request,'chemblbase/substructure_search_results.html',content)

            elif data_source == 'Inhouse':
                allosrimolecule=[]
                inhousecompounds = Osrimolecule.objects.all()
                for compound in inhousecompounds:
                    mother_mol = Chem.MolFromSmiles(compound.canonical_smiles)
                    if mother_mol.HasSubstructMatch(Chem.MolFromSmiles(sub_smiles)):
                        allosrimolecule.append(compound)

                testformset = formset_factory(TestForm,extra=len(allosrimolecule))
                formset = testformset()

                alltogether = zip(allosrimolecule,formset)
                for compound,form in alltogether:
                    form.initial['fname'] = compound.ligand_id

                logger.info(len(allosrimolecule))
                logger.info(len(formset))
                content = {'allosrimolecule':allosrimolecule,'formset':formset}
                return render(request,'chemblbase/inhouse.html',content)

                #content = {'allosrimolecule':allosrimolecule}
                #return render(request,'chemblbase/inhouse_substructure_search.html',content)
                #content = {'table_data':table_data}
                #return render(request,'chemblbase/substructure_search_results_inhouse.html',content) 


   # return render(request,'chemblbase/substructure_smile.html',{'form':form})

@login_required
def uploadfile(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            #getlast = Document.objects.last()
            #file2 = getlast.docfile
            fname = request.FILES['docfile']
            current_time =  time.strftime("%Y%m%d-%H%M%S")
            tempfilename = JXYTEMPDIR + request.user.username + current_time +'.bak'
            with open(tempfilename,'wb+') as destination:
                for chunk in fname.chunks():
                    destination.write(chunk)
            
            filetype = form.cleaned_data['file_type']
            projecttype = form.cleaned_data['project_type']
            #filename = newdoc.docfile
            #file2 = request.FILES['docfile'].read()

            logger = logging.getLogger("django")
            logger.info(filetype)
            logger.info(tempfilename) 

            if filetype == 'SDF':
                #with Chem.ForwardSDMolSupplier(file2) as suppl:
                with Chem.SDMolSupplier(tempfilename) as suppl: 
                    for mol in suppl:
                        lig_smi = Chem.MolToSmiles(mol)
                        lig_id=create_new_ref_number2()
                        logp_value = Descriptors.MolLogP(mol)
                        tpsa_value = Descriptors.TPSA(mol)
                        recorder_val = request.user.username

                        #file_path = settings.STATICFILES_DIRS[0] + '\\images\inhouse'
                        #file_path_name = file_path + '\\' + lig_id + '.png'
                        #Draw.MolToFile(mol,file_path_name)

                        q=Osrimolecule(ligand_id=lig_id,logp=logp_value,canonical_smiles=lig_smi,target_id=projecttype,tpsa=tpsa_value,recorder=recorder_val)
                        q.save()

            if filetype == 'CSV':
                suppl = pd.read_csv(tempfilename)
                for index, mol in suppl.iterrows():
                    lig_smi = mol['compound_structures.canonical_smiles']
                    m = Chem.MolFromSmiles(lig_smi)
                    if m is None: 
                        Continue
                    lig_id = create_new_ref_number2()
                    logp_value = Descriptors.MolLogP(m)
                    tpsa_value = Descriptors.TPSA(m)
                    recorder_val = request.user.username

                    #file_path = settings.STATICFILES_DIRS[0] + '\\images\inhouse'
                    #file_path_name = file_path + '\\' + lig_id + '.png'
                    #Draw.MolToFile(m,file_path_name)

                    activity_type_value = mol['activities.standard_type']
                    activity_value_value = mol['activities.standard_value']
                    activity_unit_value = mol['activities.standard_units']

                    q=Osrimolecule(ligand_id=lig_id,logp=logp_value,canonical_smiles=lig_smi,target_id=projecttype,tpsa=tpsa_value, \
                                   recorder=recorder_val,assay_type='B',activity_type=activity_type_value,activity_unit=activity_unit_value,\
                                   activity_value=activity_value_value)
                    q.save()



            #newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('chemblbase:uploadfile'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,'chemblbase/upload.html',{'documents': documents, 'form': form})


