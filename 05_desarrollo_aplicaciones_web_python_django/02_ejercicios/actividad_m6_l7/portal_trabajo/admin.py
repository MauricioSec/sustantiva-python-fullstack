from django.contrib import admin
from .models import SectorMaritimo, Departamento, CargoEspecialidad, PerfilMaritimo, OfertaEmpleo

admin.site.register(SectorMaritimo)
admin.site.register(Departamento)
admin.site.register(CargoEspecialidad)
admin.site.register(PerfilMaritimo)
admin.site.register(OfertaEmpleo)