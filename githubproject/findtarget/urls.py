from django.urls import path
from findtarget import views

urlpatterns = [
    path('', views.find_the_target, name='find_target'),
]