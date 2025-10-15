from django.urls import path
from . import views

urlpatterns = [
    # Rutas de usuarios
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),

    # Rutas de documentos
    path('documentos/', views.lista_documentos, name='lista_documentos'),
    path('documentos/crear/', views.crear_documento, name='crear_documento'),
    path('documentos/editar/<int:pk>/', views.editar_documento, name='editar_documento'),
    path('documentos/eliminar/<int:pk>/', views.eliminar_documento, name='eliminar_documento'),
]
