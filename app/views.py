# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Documento
from .forms import UsuarioForm, DocumentoForm


# INICIO 
def inicio(request):
    return render(request, 'inicio.html')


# USUARIOS 
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/formulario.html', {'form': form, 'accion': 'Crear'})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/formulario.html', {'form': form, 'accion': 'Editar'})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/eliminar.html', {'usuario': usuario})


# DOCUMENTOS
def lista_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'documentos/lista.html', {'documentos': documentos})

def crear_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_documentos')
    else:
        form = DocumentoForm()
    return render(request, 'documentos/formulario.html', {'form': form, 'accion': 'Crear'})

def editar_documento(request, pk):
    documento = get_object_or_404(Documento, pk=pk)
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES, instance=documento)
        if form.is_valid():
            form.save()
            return redirect('lista_documentos')
    else:
        form = DocumentoForm(instance=documento)
    return render(request, 'documentos/formulario.html', {'form': form, 'accion': 'Editar'})

def eliminar_documento(request, pk):
    documento = get_object_or_404(Documento, pk=pk)
    if request.method == 'POST':
        documento.delete()
        return redirect('lista_documentos')
    return render(request, 'documentos/eliminar.html', {'documento': documento})
