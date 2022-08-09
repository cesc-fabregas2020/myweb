from django.urls import path
from fuser import views

urlpatterns = [
    path('index2.html', views.fuser, name='fuser'),
]