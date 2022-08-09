from django.urls import path
from . import views

app_name = 'filtercheck'

urlpatterns = [
    path('', views.justcheck, name='justcheck'),
]