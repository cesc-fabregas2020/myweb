from django.urls import path
from . import views
 
app_name = 'lbdd'

urlpatterns = [
    path('d3gen/',views.d3gen,name='d3gen'),
    path('amesprediction/',views.amespred,name='property_prediction'),
    path('molfilter/',views.molfilter,name='molecules_filter'),
    path('stringtest/<str:strcha>/',views.strtest,name='strtest'), 
]