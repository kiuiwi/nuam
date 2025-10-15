from django.db import models


class TIPOS_USUARIOS(models.Model): 
    ID_TIPO_USUARIO = models.IntegerField(primary_key=True) 
    TIPO_USUARIO = models.CharField(max_length=15, null=True, blank=True) 

    def __str__(self):
        return self.TIPO_USUARIO or "Sin tipo"


class PAISES(models.Model): 
    ID_PAIS = models.IntegerField(primary_key=True) 
    PAIS = models.CharField(max_length=15, null=True, blank=True) 

    def __str__(self):
        return self.PAIS or "Sin país"


class REGIONES(models.Model): 
    ID_REGION = models.IntegerField(primary_key=True) 
    REGION = models.CharField(max_length=15, null=True, blank=True) 

    def __str__(self):
        return self.REGION or "Sin región"


class USUARIOS(models.Model): 
    ID_USUARIO = models.IntegerField(primary_key=True) 
    NOMBRE_USUARIO = models.CharField(max_length=15, null=True, blank=True) 
    APELLIDO_USUARIO = models.CharField(max_length=15, null=True, blank=True) 
    TELEFONO = models.IntegerField(null=True, blank=True) 
    EMAIL = models.EmailField(null=True, blank=True) 
    DIRECCION = models.CharField(max_length=30, null=True, blank=True) 
    ID_TIPO_USUARIO = models.ForeignKey(TIPOS_USUARIOS, on_delete=models.CASCADE, to_field='ID_TIPO_USUARIO') 
    ID_PAIS = models.ForeignKey(PAISES, on_delete=models.CASCADE, to_field='ID_PAIS') 
    ID_REGION = models.ForeignKey(REGIONES, on_delete=models.CASCADE, to_field='ID_REGION') 

    def __str__(self):
        return f"{self.NOMBRE_USUARIO} {self.APELLIDO_USUARIO}".strip() or "Usuario sin nombre"


class TIPOS_DOCUMENTOS(models.Model): 
    ID_TIPO_DOCUMENTO = models.IntegerField(primary_key=True) 
    TIPO_DOCUMENTO = models.CharField(max_length=30, null=True, blank=True) 

    def __str__(self):
        return self.TIPO_DOCUMENTO or "Sin tipo"


class DOCUMENTOS(models.Model): 
    ID_DOCUMENTO = models.IntegerField(primary_key=True) 
    NOMBRE_DOCUMENTO = models.CharField(max_length=50, null=True, blank=True) 
    FECHA_INGRESO = models.DateField(null=True, blank=True) 
    ID_USUARIO = models.ForeignKey(USUARIOS, on_delete=models.CASCADE, to_field='ID_USUARIO') 
    ID_TIPO_DOCUMENTO = models.ForeignKey(TIPOS_DOCUMENTOS, on_delete=models.CASCADE, to_field='ID_TIPO_DOCUMENTO') 

    def __str__(self):
        return f"{self.NOMBRE_DOCUMENTO} ({self.ID_TIPO_DOCUMENTO})" if self.NOMBRE_DOCUMENTO else "Documento sin nombre"


class HISTORIAL_CAMBIOS(models.Model): 
    ID_HISTORIAL = models.IntegerField(primary_key=True) 
    FECHA_MODIFICACION = models.DateField(null=True, blank=True) 
    FECHA_ELIMINAR = models.DateField(null=True) 
    ID_USUARIO = models.ForeignKey(USUARIOS, on_delete=models.CASCADE, to_field='ID_USUARIO') 
    ID_DOCUMENTO = models.ForeignKey(DOCUMENTOS, on_delete=models.CASCADE, to_field='ID_DOCUMENTO') 

    def __str__(self):
        return f"Historial #{self.ID_HISTORIAL} - Usuario: {self.ID_USUARIO}"
