from django.contrib import admin
from chemblbase.models import Document,wntmolecule,thankspic
# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    pass

class wntmoleculeAdmin(admin.ModelAdmin):
    pass

class thankspicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Document,DocumentAdmin) 
admin.site.register(wntmolecule,wntmoleculeAdmin)
admin.site.register(thankspic,thankspicAdmin)