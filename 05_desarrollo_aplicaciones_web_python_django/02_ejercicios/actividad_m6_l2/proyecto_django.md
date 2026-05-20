# Registro de Creación y Configuración: mi_sitio

## 1. Instalación en entorno virtual

**Comandos ejecutados y su función:**

1. `python -m venv env`: Instruye al intérprete de Python para ejecutar el módulo integrado `venv` y crear un nuevo directorio llamado `env`, el cual contendrá un entorno virtual aislado.
2. `source env/bin/activate` (Linux/macOS) o `env\Scripts\activate` (Windows): Modifica las variables de entorno de la sesión actual de la terminal para que los comandos de Python y pip utilicen los binarios locales de la carpeta `env` en lugar de los globales del sistema operativo.
3. `pip install django`: Utiliza el gestor de paquetes para descargar la última versión estable de Django desde el repositorio oficial (PyPI) y la instala dentro del entorno virtual activo.
4. `django-admin --version`: Comando de verificación que devuelve la versión instalada de Django, confirmando que el framework está operativo y en el PATH del entorno.

**¿Qué es pip?**
PIP (*Pip Installs Packages*) es el sistema de gestión de paquetes estándar y oficial escrito en Python, utilizado para instalar y administrar bibliotecas de software o dependencias que no forman parte de la biblioteca estándar de Python.

**Ventajas de instalar Django en un entorno virtual:**
- **Aislamiento de dependencias:** Evita conflictos de versiones si tienes múltiples proyectos en la misma máquina que requieren distintas versiones de Django.
- **Limpieza del sistema:** Evita contaminar la instalación global de Python en tu sistema operativo.
- **Replicabilidad:** Permite generar un archivo `requirements.txt` exacto, garantizando que el entorno de desarrollo sea idéntico al entorno de producción o al de otros desarrolladores.

## 2. Crear el proyecto

**Comando de creación:** `django-admin startproject mi_sitio`

**Estructura generada y su propósito:**

```text
mi_sitio/
    manage.py
    mi_sitio/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py