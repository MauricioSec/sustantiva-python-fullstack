Proyecto Blog - Módulo 7
-------------------------

Descripción:
Implementación de un modelo de datos basado en el modelo de Blog, utilizando las entidades Autor y Articulo. El proyecto fue desarrollado sobre el framework Django con una base de datos PostgreSQL.

Pasos seguidos:
1. Creación y activación de entorno virtual (venv).
2. Instalación de dependencias: django y psycopg2-binary.
3. Configuración del proyecto Django y creación de la aplicación 'blog'.
4. Configuración de la conexión a PostgreSQL en settings.py.
5. Definición de los modelos Autor y Articulo en models.py con una relación ForeignKey.
6. Aplicación de migraciones mediante los comandos makemigrations y migrate.
7. Verificación de operaciones CRUD y consultas ORM mediante el shell interactivo de Django.

Estructura del Proyecto:
- blog_project/ : Configuración del proyecto Django.
- blog/ : Aplicación con los modelos y lógica de datos.
- manage.py : Script de administración de Django.
- Captura_consola.png : Evidencia de la ejecución de comandos y consultas ORM.