from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

ASSAY_TYPE_CHOICES=[
    ('',''),
    ('A','ADME'),
    ('B','Binding'),
    ('F','Functional'),
    ('P','Physiochemical'),
    ('T','Toxicity'),
    ('C','Computer Calculation'),
    ('U','Unassigned'),
]

ACTIVITY_TYPE_CHOICES=[
    ('IC50','IC50'),
    ('EC50','EC50'),
    ('AC50','AC50'),
    ('GI50','GI50'), 
    ('Ki','Ki'),
]

TARGET_TYPE_CHOICES=[
    ('',''),
    ('RIPK1','RIPK1'),
    ('TLR7','TLR7'),
    ('TLR8','TLR8'),
    ('TLR9','TLR9'), 
    ('WNT','WNT'),
    ('KRAS','KRAS'),
    ('LXR','LXR'),
]

class OsriMoleculeForm(forms.Form):
    ligand_id = forms.CharField(max_length=100,label='Ligand ID',required=False)
    ligand = forms.CharField(max_length=4000,initial='please enter smile',widget=forms.TextInput(attrs={'id':'myinput'}))
    target = forms.CharField(max_length=200, label='what is your target?',widget=forms.Select(choices=TARGET_TYPE_CHOICES))
    assay_type=forms.CharField(label='what is your assay type?',widget=forms.Select(choices=ASSAY_TYPE_CHOICES))
    activity_type=forms.CharField(label='what is your activity type?',widget=forms.Select(choices=ACTIVITY_TYPE_CHOICES)) 
    activity_value=forms.DecimalField(max_digits=7, decimal_places=2, required=False)
    activity_unit=forms.CharField(max_length=20,label='Activity Unit', required=False)
    disease =  forms.CharField(max_length=4000,initial='please enter the disease')
    descriptions = forms.CharField(widget=forms.Textarea,max_length=4000,initial='please enter the descriptions')


DATASOURCE_CHOICES=[
    ('Chembl27','Chembl27'),
    ('Inhouse','Inhouse'),
]

class MolSmile(forms.Form): 
    ligand_smile = forms.CharField(max_length=4000,label='Template Smile',widget=forms.TextInput(attrs={'id':'myinput'}))
    datasource = forms.CharField(label='please select the database',widget=forms.Select(choices=DATASOURCE_CHOICES))

FILE_TYPE_CHOICES=[
    ('SDF','SDF'),
    ('MOL','MOL'),
    ('CSV','CSV'),
    ('PDB','PDB'),
    ('TXT','TXT'),
]

PROJECT_TYPE_CHOICES=[
    ('RIPK1_001','RIPK1_001'),
    ('TNIK_001','TNIK_001'),
    ('LXR','LXR'),
    ('TLR7','TLR7'),
    ('TLR8','TLR8'),
    ('KRAS','KRAS'),
    ('WNT','WNT'),
]

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file',)
    file_type = forms.CharField(label='File type',widget=forms.Select(choices=FILE_TYPE_CHOICES))
    project_type = forms.CharField(label='Project',widget=forms.Select(choices=PROJECT_TYPE_CHOICES))


class AdvancedSearchForm(forms.Form):
    AS_ligand_id  = forms.CharField(max_length=100,label='Ligand ID',required=False)
    AS_target_id  = forms.CharField(max_length=200,label='Target ID',widget=forms.Select(choices=TARGET_TYPE_CHOICES),required=False)
    AS_assay_type = forms.CharField(label='Assay Type',widget=forms.Select(choices=ASSAY_TYPE_CHOICES),required=False)
    AS_recorder   = forms.CharField(label='Recorder',max_length=50,required=False)

class TestForm(forms.Form):
    fname = forms.CharField(widget=forms.HiddenInput(),required=False)
    slect = forms.BooleanField(required=False,label=False)