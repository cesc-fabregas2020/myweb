from django.urls import path
from ourdatabase import views

urlpatterns = [
    path('', views.test, name='database_test'),
]