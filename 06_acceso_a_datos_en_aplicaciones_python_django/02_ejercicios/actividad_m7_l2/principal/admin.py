from django.contrib import admin
from .models import Libro

# Registramos el modelo para que sea visible en el panel de administración
admin.site.register(Libro)