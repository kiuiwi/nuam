

NUAM 
(Gestión de Usuarios y Documentos)

Este proyecto fue desarrollado en Django 5.1.4 y permite gestionar usuarios y documentos, incluyendo creación, edición, eliminación y visualización de registros.




1. Requisitos previos
Antes de ejecutar el proyecto, asegúrate de tener instalado:

Python 3.12 o superior
pip (administrador de paquetes de Python)
Git
Virtualenv (opcional pero recomendado)



2. Clonar el repositorio
Crea una carpeta donde guardarás el proyecto

Abre una terminal y accede a la carpeta creada, luego ejecuta:
git clone https://github.com/kiuiwi/nuam

cd nuam



3. Crear y activar entorno virtual 
Desde la misma carpeta del proyecto "nuam", ejecuta:
Linux/Mac:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate



4. Instalar Django
pip install Django


Verificar versión:
django-admin --version
(debiese ser igual o superior a la 5.1.4)


5. Ejecutar el servidor
Windows:
python manage.py runserver

Linux/Mac:
python3 manage.py runserver




Accede en el navegador a:  http://127.0.0.1:8000/



Credenciales de Admin 
usuario: inacap
correo: inacap@inacap.cl
contraseña: inacap123




💡 Notas
El proyecto incluye un CRUD completo para usuarios y documentos.
El archivo .gitignore excluye venv/, __pycache__/, db.sqlite3 y otros archivos innecesarios.



✨ Autores:
Nombres: Sol Toledo, Camila Cruz, Alejandra Miranda
Carrera: Analista Programador
Institución: Inacap
Año: 2025
