from django.urls import path
from leadopt import views

urlpatterns = [
    path('', views.leadopt, name='leadopt'),
]