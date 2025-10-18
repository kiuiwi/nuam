from django.db import models



class UsuarioTipo(models.Model):
    id_usuario_tipo = models.AutoField(primary_key=True, db_column='ID_USUARIO_TIPO')
    usuario_tipo = models.CharField(max_length=30, blank=True, db_column='USUARIO_TIPO')

    def __str__(self):
        return self.usuario_tipo or "Tipo sin nombre"

    class Meta:
        verbose_name = 'Tipo de Usuario'
        verbose_name_plural = 'Tipos de Usuario'



class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True, db_column='ID_PAIS')
    pais = models.CharField(max_length=50, blank=True, db_column='PAIS')

    def __str__(self):
        return self.pais or "País sin nombre"

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'



class Region(models.Model):
    id_region = models.AutoField(primary_key=True, db_column='ID_REGION')
    region = models.CharField(max_length=50, blank=True, db_column='REGION')

    def __str__(self):
        return self.region or "Región sin nombre"

    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'



class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, db_column='ID_USUARIO')
    usuario_tipo = models.ForeignKey(UsuarioTipo, on_delete=models.SET_NULL, null=True, blank=True, db_column='ID_USUARIO_TIPO')
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True, db_column='ID_PAIS')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, db_column='ID_REGION')
    usuario_nombre = models.CharField(max_length=50, blank=True, db_column='USUARIO_NOMBRE')
    usuario_apellido = models.CharField(max_length=50, blank=True, db_column='USUARIO_APELLIDO')
    telefono = models.CharField(max_length=20, blank=True, db_column='TELEFONO')
    email = models.EmailField(blank=True, db_column='EMAIL')
    direccion = models.CharField(max_length=100, blank=True, db_column='DIRECCION')

    def __str__(self):
        nombre = f"{self.usuario_nombre} {self.usuario_apellido}".strip()
        return nombre or f"Usuario {self.id_usuario}"

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'




class DocumentoTipo(models.Model):
    id_documento_tipo = models.AutoField(primary_key=True, db_column='ID_DOCUMENTO_TIPO')
    documento_tipo = models.CharField(max_length=50, blank=True, db_column='DOCUMENTO_TIPO')

    def __str__(self):
        return self.documento_tipo or "Tipo sin nombre"

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'




class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True, db_column='ID_DOCUMENTO')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='ID_USUARIO')
    documento_nombre = models.CharField(max_length=100, blank=True, db_column='DOCUMENTO_NOMBRE')
    documento_tipo = models.ForeignKey(DocumentoTipo, on_delete=models.SET_NULL, null=True, blank=True, db_column='ID_DOCUMENTO_TIPO')
    archivo = models.FileField(upload_to='documentos/', blank=True, null=True, db_column='ARCHIVO')
    fecha_ingreso = models.DateTimeField(auto_now_add=True, db_column='FECHA_INGRESO')

    def __str__(self):
        return self.documento_nombre or "Documento sin título"

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
