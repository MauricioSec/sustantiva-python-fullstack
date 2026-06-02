from django.urls import path
from .views import InicioView, PanelPrivadoView, PanelAvanzadoView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('privado/', PanelPrivadoView.as_view(), name='privado'),
    path('avanzado/', PanelAvanzadoView.as_view(), name='avanzado'),
]