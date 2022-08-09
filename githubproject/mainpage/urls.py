from django.urls import path
from django.urls import path
from mainpage import views

urlpatterns = [
    path('',views.main_page,name='main_page'),
]