from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Punto 3.2: Registro de Usuario
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente. Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cuentas/registro.html', {'form': form})

# Punto 3.3: Vista Protegida (Panel del Usuario)
@login_required # Este decorador bloquea el acceso a usuarios no autenticados
def dashboard(request):
    return render(request, 'cuentas/dashboard.html')