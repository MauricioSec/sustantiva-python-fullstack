from django.urls import path
from . import views

urlpatterns = [
    # Ruta raíz de la app: mostrará la lista
    path('', views.listar_libros, name='listar_libros'),
    
    # Rutas para modificar datos
    path('crear/', views.crear_libro, name='crear_libro'),
    path('editar/<int:id>/', views.editar_libro, name='editar_libro'),
    path('eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
]