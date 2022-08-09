from django.contrib import admin
from lbdd.models import PropertyDocument
# Register your models here.

class PropertyDocumentAdmin(admin.ModelAdmin):
    pass

admin.site.register(PropertyDocument,PropertyDocumentAdmin) 