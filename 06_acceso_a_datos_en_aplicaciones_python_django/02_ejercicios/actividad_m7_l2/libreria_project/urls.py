from django.contrib import admin
from django.urls import path, include  # <-- Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Conectamos las rutas de la app 'libros' al prefijo '/libros/'
    path('libros/', include('libros.urls')), 
]