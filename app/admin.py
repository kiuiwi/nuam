from django.contrib import admin
from .models import *

admin.site.register(USUARIOS)
admin.site.register(DOCUMENTOS)
admin.site.register(TIPOS_USUARIOS)
admin.site.register(PAISES)     
admin.site.register(REGIONES)   
admin.site.register(TIPOS_DOCUMENTOS)
admin.site.register(HISTORIAL_CAMBIOS)  

