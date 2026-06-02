from django.shortcuts import render
from .forms import ContactoForm

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'actividad_m6_l4/contacto.html', {'form': ContactoForm(), 'exito': 'Mensaje enviado correctamente.'})
    else:
        form = ContactoForm()
    return render(request, 'actividad_m6_l4/contacto.html', {'form': form})