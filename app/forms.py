from django import forms
from .models import Usuario, Documento



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'usuario_nombre',
            'usuario_apellido',
            'telefono',
            'email',
            'direccion',
            'usuario_tipo',
            'pais',
            'region',
        )



class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = (
            'usuario',
            'documento_nombre',
            'documento_tipo',
            'archivo',
        )
