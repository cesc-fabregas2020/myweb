from django.urls import path
from . import views

app_name = 'jsmetest'

urlpatterns = [
    path('', views.drawpic, name='drawpic'),
]