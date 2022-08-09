from pyexpat import model
from django.db import models

# Create your models here.

class PropertyDocument(models.Model):
    docfile = models.FileField()

class FilterDocument(models.Model):
    passed_file = models.FileField()
    error_file = models.FileField()