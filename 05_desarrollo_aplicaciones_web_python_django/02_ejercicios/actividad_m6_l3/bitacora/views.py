from django.shortcuts import render
from django.http import HttpResponse
from .forms import InspeccionForm

def panel_inicio(request):
    return render(request, 'bitacora/inicio.html')

def registrar_inspeccion(request):
    if request.method == 'POST':
        formulario = InspeccionForm(request.POST)
        if formulario.is_valid():
            formulario.save() # Esta única línea inserta los datos en la base de datos
            equipo = formulario.cleaned_data['equipo']
            return HttpResponse(f"Inspección guardada permanentemente en la base de datos para el equipo: {equipo}")
    else:
        formulario = InspeccionForm()

    return render(request, 'bitacora/registro.html', {'form': formulario})