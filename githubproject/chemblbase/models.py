from django.db import models
from django.db.models.base import Model

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class wntmolecule(models.Model):
    imgfile = models.FileField(upload_to='image/thanks')

class thankspic(models.Model):
    imgfile = models.FileField(upload_to='image/thanks') 