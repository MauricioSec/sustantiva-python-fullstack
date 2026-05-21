from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Rutas de autenticación (Punto 3.1)
    path('login/', LoginView.as_view(template_name='cuentas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Ruta de registro (Punto 3.2)
    path('registro/', views.registro, name='registro'),
    
    # Ruta protegida (Punto 3.3)
    path('dashboard/', views.dashboard, name='dashboard'),
]