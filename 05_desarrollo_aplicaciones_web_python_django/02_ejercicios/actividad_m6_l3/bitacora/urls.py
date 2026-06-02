from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel_inicio, name='inicio'),
    path('registrar/', views.registrar_inspeccion, name='registrar_inspeccion'),
]