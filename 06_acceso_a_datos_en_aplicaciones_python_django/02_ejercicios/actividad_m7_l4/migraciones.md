# Actividad N° 4 – Gestión de Migraciones en Django

## 1. Comprensión teórica

* **¿Qué es una migración en Django?**
  Es el sistema de control de versiones para el esquema de la base de datos. Consiste en archivos de Python que Django genera automáticamente para traducir las estructuras de código definidas en `models.py` a instrucciones SQL ejecutables.

* **¿Qué problema soluciona respecto a los cambios en los modelos?**
  Soluciona la inconsistencia entre el código fuente y el almacenamiento persistente. Permite evolucionar la base de datos (añadir campos, modificar restricciones) de forma segura y estructurada.

* **¿Por qué no basta con modificar el archivo models.py directamente sin hacer migraciones?**
  Porque `models.py` es solo la representación en Python. PostgreSQL funciona con tablas físicas. Si no se aplican las migraciones, el framework intentará leer columnas que no existen en la base de datos, provocando errores fatales.

## 2. Crear y aplicar migraciones

**a) Código añadido al modelo Libro:**
`isbn = models.CharField(max_length=13, null=True, blank=True)`

**b) Comandos ejecutados:**
* `python manage.py makemigrations`: Detectó el nuevo campo y creó el archivo de migración `0002_libro_isbn.py`.
* `python manage.py migrate`: Ejecutó las instrucciones SQL en PostgreSQL para agregar la columna exitosamente (`Applying principal.0002_libro_isbn... OK`).

## 3. Aplicar migraciones existentes (Prueba Práctica)

**Procedimiento realizado:** Se eliminó físicamente el archivo de migración `0002_libro_isbn.py` de la carpeta `migrations/` y se volvieron a ejecutar los comandos `makemigrations` y `migrate`.

**Resultado obtenido:**
* `makemigrations` recreó el archivo con el mismo nombre (`0002_libro_isbn.py`).
* `migrate` arrojó el mensaje: `No migrations to apply.`

**Análisis del comportamiento:**
El sistema no arrojó un error de base de datos debido al control interno de Django. Al aplicarse la primera migración, Django guardó un registro en su tabla `django_migrations`. Al recrearse un archivo con el **mismo nombre exacto**, el comando `migrate` detectó que esa migración ya figuraba como "aplicada" en su historial interno, por lo que omitió ejecutar las instrucciones SQL nuevamente, protegiendo así la base de datos de un error de redundancia.

## 4. Revisión de estado

* **Comando ejecutado:** `python manage.py showmigrations`
* **Información entregada:** Despliega una lista de todas las aplicaciones y sus archivos de migración. Las migraciones que ya están registradas en la base de datos como aplicadas aparecen con una marca `[X]`.