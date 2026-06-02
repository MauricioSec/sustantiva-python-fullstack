from django import forms
from .models import ConsultaContacto

class ContactoForm(forms.ModelForm):
    
    mensaje = forms.CharField(widget=forms.Textarea, min_length=10)

    class Meta:
        model = ConsultaContacto
        fields = ['nombre', 'correo', 'mensaje']