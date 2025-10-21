from django.contrib import admin
from .models import UsuarioTipo, Pais, Region, Usuario, DocumentoTipo, Documento



@admin.register(UsuarioTipo)
class UsuarioTipoAdmin(admin.ModelAdmin):
    list_display = ('id_usuario_tipo', 'usuario_tipo')
    search_fields = ('usuario_tipo',)
    ordering = ('usuario_tipo',)



@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id_pais', 'pais')
    search_fields = ('pais',)
    ordering = ('pais',)



@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id_region', 'region')
    search_fields = ('region',)
    ordering = ('region',)



@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'id_usuario',
        'usuario_nombre',
        'usuario_apellido',
        'telefono',
        'email',
        'direccion',
        'get_region',
        'get_pais',
        'get_usuario_tipo',
    )
    search_fields = (
        'usuario_nombre',
        'usuario_apellido',
        'usuario_tipo__usuario_tipo',
        'region__region',
        'pais__pais',
    )
    list_filter = ('usuario_tipo', 'pais', 'region')
    ordering = ('usuario_nombre',)


    def get_region(self, obj):
        return obj.region.region if obj.region else ''
    get_region.short_description = 'Región'

    def get_pais(self, obj):
        return obj.pais.pais if obj.pais else ''
    get_pais.short_description = 'País'

    def get_usuario_tipo(self, obj):
        return obj.usuario_tipo.usuario_tipo if obj.usuario_tipo else ''
    get_usuario_tipo.short_description = 'Tipo de Usuario'




@admin.register(DocumentoTipo)
class DocumentoTipoAdmin(admin.ModelAdmin):
    list_display = ('id_documento_tipo', 'documento_tipo')
    search_fields = ('documento_tipo',)
    ordering = ('documento_tipo',)



@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id_documento', 'documento_nombre', 'usuario', 'documento_tipo', 'fecha_ingreso')
    search_fields = ('documento_nombre', 'usuario__usuario_nombre', 'usuario__usuario_apellido')
    list_filter = ('documento_tipo', 'fecha_ingreso')
    ordering = ('fecha_ingreso',)
