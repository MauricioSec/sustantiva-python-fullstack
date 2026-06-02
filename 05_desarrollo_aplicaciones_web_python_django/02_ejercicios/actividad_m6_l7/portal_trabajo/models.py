from django.db import models
from django.contrib.auth.models import User

# --- 1. JERARQUÍA MARÍTIMA ESTRICTA ---

class SectorMaritimo(models.Model):
    nombre = models.CharField(max_length=100, unique=True, help_text="Ej: Marina Mercante, Naves Menores, Pesca Industrial")

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    sector = models.ForeignKey(SectorMaritimo, on_delete=models.CASCADE, related_name='departamentos')
    nombre = models.CharField(max_length=100, help_text="Ej: Oficiales de Cubierta, Mando, Tripulación")

    def __str__(self):
        return f"{self.nombre} ({self.sector.nombre})"

class CargoEspecialidad(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='cargos')
    nombre = models.CharField(max_length=100, help_text="Ej: Patrón de Nave Menor, Piloto Primero")

    def __str__(self):
        return f"{self.nombre} - {self.departamento.sector.nombre}"


# --- 2. PERFILES Y OFERTAS DE EMPLEO ---

class PerfilMaritimo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    # Relación estricta con la jerarquía legal
    cargo_actual = models.ForeignKey(CargoEspecialidad, on_delete=models.SET_NULL, null=True, blank=True)
    
    libreta_embarque = models.CharField(max_length=50, blank=True, null=True, help_text="N° de Libreta o Matrícula")
    puerto_base = models.CharField(max_length=100, blank=True, null=True, help_text="Ej: Puerto Montt")
    experiencia_anios = models.PositiveIntegerField(default=0)

    def __str__(self):
        cargo_str = self.cargo_actual.nombre if self.cargo_actual else "Sin cargo definido"
        return f"{self.user.username} - {cargo_str}"

class OfertaEmpleo(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ofertas_publicadas')
    # La oferta exige un cargo legal específico
    cargo_solicitado = models.ForeignKey(CargoEspecialidad, on_delete=models.CASCADE)
    
    nave_o_proyecto = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    salario_ofrecido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"Busco: {self.cargo_solicitado.nombre} para {self.nave_o_proyecto}"