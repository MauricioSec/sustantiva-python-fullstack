from django import forms
from .models import Inspeccion # Importamos el modelo recién creado

class InspeccionForm(forms.ModelForm):
    class Meta:
        model = Inspeccion
        fields = ['equipo', 'horas_operacion', 'observaciones']

    # Mantenemos intacta la validación backend exigida en la rúbrica
    def clean_horas_operacion(self):
        horas = self.cleaned_data.get('horas_operacion')
        if horas < 0:
            raise forms.ValidationError("Las horas de operación no pueden ser negativas.")
        return horas