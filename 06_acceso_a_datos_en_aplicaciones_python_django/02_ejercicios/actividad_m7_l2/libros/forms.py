from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'anio']
        labels = {
            'titulo': 'Título del Libro',
            'autor': 'Autor',
            'anio': 'Año de Publicación',
        }