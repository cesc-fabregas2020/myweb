from django import forms

CHIRALITY_SOURCE_TYPE=[
    ('Keep','Keep'),
    ('Enumerate','Enumerate'),
]

CONFORMATION_TYPE=[
    ('2D','2D'),
    ('3D','3D'),
] 

class ConfGenForm(forms.Form):
    chirality_source = forms.CharField(label='Enumerate chirality or not ?', widget=forms.Select(choices=CHIRALITY_SOURCE_TYPE))
    conf_type = forms.CharField(label='2D or 3D', widget=forms.Select(choices=CONFORMATION_TYPE))
    docfile = forms.FileField(label='Select a sdf file')

CHEMPROP_TYPE=[
    ('Train','Train'),
    ('Predict','Predict'),
]

class AmesForm(forms.Form):
    docfile = forms.FileField(label='Select a file',required=False)
    compounds = forms.CharField(widget=forms.Textarea,required=False)

class MolFilterForm(forms.Form):
    docfile = forms.FileField(label='Select a file',required=True)
    