from django import forms
from .models import USUARIOS, DOCUMENTOS

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = USUARIOS
        fields = '__all__'


class DocumentoForm(forms.ModelForm):
    FECHA_INGRESO = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = DOCUMENTOS
        fields = '__all__'
