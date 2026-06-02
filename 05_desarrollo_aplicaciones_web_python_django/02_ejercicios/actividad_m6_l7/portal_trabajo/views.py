from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import OfertaEmpleo

def vista_inicio(request):
    # Recupera solo las ofertas que están activas
    ofertas = OfertaEmpleo.objects.filter(activa=True).order_by('-fecha_publicacion')
    return render(request, 'portal_trabajo/inicio.html', {'ofertas': ofertas})

@login_required
def vista_contacto(request):
    return render(request, 'portal_trabajo/contacto.html')