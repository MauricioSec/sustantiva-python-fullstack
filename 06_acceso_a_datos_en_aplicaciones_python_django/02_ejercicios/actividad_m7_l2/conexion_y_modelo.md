# Actividad N° 2 – Conexión a Base de Datos y Uso del ORM en Django

## 1. Conexión a PostgreSQL
Para establecer la conexión, se instaló el adaptador necesario mediante el comando:
`pip install psycopg2-binary`

En el archivo `settings.py` del proyecto, se actualizó el diccionario `DATABASES` para conectar con el motor PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'libreria',
        'USER': 'usuario_db',
        'PASSWORD': 'password_seguro',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}