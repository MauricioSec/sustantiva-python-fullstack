from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    anio = models.IntegerField()

    class Meta:
        ordering = ['id']  # Fuerza a ordenar siempre por el ID de creación

    def __str__(self):
        return self.titulo