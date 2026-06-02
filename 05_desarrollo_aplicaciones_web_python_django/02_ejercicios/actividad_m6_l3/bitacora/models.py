from django.db import models

class Inspeccion(models.Model):
    equipo = models.CharField(max_length=50, verbose_name="Equipo a inspeccionar")
    horas_operacion = models.IntegerField(verbose_name="Horas de operación")
    observaciones = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipo} - {self.fecha_registro.strftime('%d-%m-%Y')}"