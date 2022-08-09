from django.urls import path
from . import views
 
app_name = 'chemblbase'
 
urlpatterns = [
    path('', views.chemblmainpage, name='chemblmainpage'),
    path('compound/',views.compound,name='dashboard'),
    path('index/<int:kinase_id>',views.index,name='index'),
    path('kinase/',views.allkinase,name='kinase'),
    path('singlemolecule/<str:chemblid>',views.singlemolecule,name='singlemolecule'),
    path('singlemoleculeosri/<str:chemblid>',views.singlemoleculeosri,name='singlemoleculeosri'),
    path('contact/',views.get_contact,name='contact'),
    path('addmol/',views.get_mol,name='addmol'),
    path('addmol/thanks',views.showthanks,name='showthanks'),
    path('drawmolecule/',views.drawmolecule,name='drawmolecule'),
    path('inhousecompound/',views.showinhouse,name='inhousecompound'),
    path('jme_window/',views.jmewindow,name='jme_window'),
    path('substrcuture_search',views.substructure_search,name='substructure_search'),
    path('substructure_search/results',views.substructure_search_results,name='substructure_search_results'),
    path('fileupload/',views.uploadfile,name='uploadfile'),
    path('delmol/',views.delmol,name='delmol'),
    path('editmol/',views.editmol,name='editmol'),
    path('asinhouse/',views.as_inhouse,name='asinhouse'),
    path('adsearch/',views.ad_search,name='adsearch'),
    path('exportfile/',views.exportfile,name='exportfile'),
] 