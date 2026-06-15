import os
import sys
import django
from django.db import connection
from django.db.models import Count

# --- CONFIGURACIÓN DEL ENTORNO ---
# 1. Obtenemos la ruta absoluta de la carpeta actual (actividad_m7_l5)
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# 2. Calculamos la ruta del proyecto Django (actividad_m7_l2)
directorio_proyecto = os.path.join(directorio_actual, '..', 'actividad_m7_l2')
# 3. Añadimos la ruta al PATH de Python para que encuentre las aplicaciones
sys.path.append(os.path.abspath(directorio_proyecto))

# 4. Configuramos el módulo de settings (proyecto libreria_project)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libreria_project.settings') 
django.setup()

# Importamos el modelo DESPUÉS de inicializar Django
from principal.models import Libro

def ejecutar_ejercicios():
    print("--- 1. Recuperación de registros ---")
    
    # Recupera todos los libros registrados.
    todos_los_libros = Libro.objects.all()
    print("Todos los libros:", todos_los_libros)

    # Recupera solo los libros cuyo autor sea "Gabriel García Márquez".
    libros_garcia_marquez = Libro.objects.filter(autor="Gabriel García Márquez")
    print("Libros de GGM:", libros_garcia_marquez)

    # Recupera los libros publicados después del año 2000. (gt = greater than)
    libros_recientes = Libro.objects.filter(anio_publicacion__gt=2000)
    print("Libros > año 2000:", libros_recientes)

    print("\n--- 2. Filtros y exclusiones ---")
    
    # Aplica un filtro para mostrar solo libros disponibles.
    libros_disponibles = Libro.objects.filter(disponible=True)
    print("Libros disponibles:", libros_disponibles)

    # Excluye todos los libros publicados antes de 1950. (lt = less than)
    libros_no_antiguos = Libro.objects.exclude(anio_publicacion__lt=1950)
    print("Libros excluyendo < 1950:", libros_no_antiguos)

    print("\n--- 3. Consultas personalizadas con SQL ---")
    
    # Ejecuta consulta SQL directa utilizando raw().
    # El formato de tabla es 'app_modelo' en minúsculas.
    libros_ordenados = Libro.objects.raw('SELECT * FROM principal_libro ORDER BY titulo;')
    print("Libros ordenados por título (RAW):")
    for libro in libros_ordenados:
        print(f" - {libro.titulo}")

    # Usa connection.cursor() para ejecutar una query personalizada.
    with connection.cursor() as cursor:
        cursor.execute('SELECT autor, COUNT(*) FROM principal_libro GROUP BY autor;')
        resultados_cursor = cursor.fetchall()
        print("Conteo por autor (Cursor):", resultados_cursor)

    print("\n--- 4. Campos específicos y anotaciones ---")
    
    # Recupera solo los títulos de todos los libros utilizando values().
    solo_titulos = Libro.objects.values('titulo')
    print("Solo títulos:", list(solo_titulos))

    # Agrega una anotación para contar cuántos libros hay por autor.
    conteo_anotado = Libro.objects.values('autor').annotate(total_libros=Count('id'))
    print("Conteo por autor (Annotate):", list(conteo_anotado))

if __name__ == '__main__':
    ejecutar_ejercicios()