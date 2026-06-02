from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class InicioView(TemplateView):
    template_name = 'core/inicio.html'

class PanelPrivadoView(LoginRequiredMixin, TemplateView):
    template_name = 'core/panel.html'

class PanelAvanzadoView(PermissionRequiredMixin, TemplateView):
    template_name = 'core/avanzado.html'
    # Exige un permiso específico registrado en el modelo Auth
    permission_required = 'auth.add_user'