

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def inicio(request):
    return render(request, 'app/inicio.html')


# --- USUARIOS ---
# Listar
def lista_usuarios(request):
    usuarios = USUARIOS.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

# Crear
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/formulario.html', {'form': form, 'accion': 'Crear'})

# Editar
def editar_usuario(request, pk):
    usuario = get_object_or_404(USUARIOS, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/formulario.html', {'form': form, 'accion': 'Editar'})

# Eliminar
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(USUARIOS, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/eliminar.html', {'usuario': usuario})




# --- DOCUMENTOS ---

# Listar documentos
def lista_documentos(request):
    documentos = DOCUMENTOS.objects.all()
    return render(request, 'documentos/lista.html', {'documentos': documentos})

# Crear documento
def crear_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.ID_USUARIO = request.user  # si estás usando el User de Django
            doc.save()
            return redirect('lista_documentos')
    else:
        form = DocumentoForm()
    return render(request, 'documentos/formulario.html', {'form': form, 'accion': 'Crear'})


# Editar documento
def editar_documento(request, pk):
    documento = get_object_or_404(DOCUMENTOS, pk=pk)
    if request.method == 'POST':
        form = DocumentoForm(request.POST, instance=documento)
        if form.is_valid():
            form.save()
            return redirect('lista_documentos')
    else:
        form = DocumentoForm(instance=documento)
    return render(request, 'documentos/formulario.html', {'form': form, 'accion': 'Editar'})

# Eliminar documento
def eliminar_documento(request, pk):
    documento = get_object_or_404(DOCUMENTOS, pk=pk)
    if request.method == 'POST':
        documento.delete()
        return redirect('lista_documentos')
    return render(request, 'documentos/eliminar.html', {'documento': documento})
