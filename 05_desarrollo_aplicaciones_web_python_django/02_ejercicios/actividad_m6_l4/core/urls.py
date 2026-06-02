from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', include('actividad_m6_l4.urls')),
]