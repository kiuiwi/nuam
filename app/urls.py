from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # Usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:pk>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),

    # Documentos
    path('documentos/', views.lista_documentos, name='lista_documentos'),
    path('documentos/nuevo/', views.crear_documento, name='crear_documento'),
    path('documentos/<int:pk>/editar/', views.editar_documento, name='editar_documento'),
    path('documentos/<int:pk>/eliminar/', views.eliminar_documento, name='eliminar_documento'),
]
