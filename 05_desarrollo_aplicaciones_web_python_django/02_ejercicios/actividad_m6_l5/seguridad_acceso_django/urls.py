from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas nativas de Auth (Login/Logout)
    path('cuentas/', include('django.contrib.auth.urls')), 
    # Rutas de la aplicación
    path('', include('core.urls')),
]