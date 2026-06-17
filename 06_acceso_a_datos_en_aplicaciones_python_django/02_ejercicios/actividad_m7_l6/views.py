from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

# READ: Mostrar todos los libros
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros})

# CREATE: Añadir un nuevo libro
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/formulario_libro.html', {'form': form})

# UPDATE: Editar un libro existente
def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/formulario_libro.html', {'form': form})

# DELETE: Eliminar un libro
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'libros/confirmar_eliminacion.html', {'libro': libro})