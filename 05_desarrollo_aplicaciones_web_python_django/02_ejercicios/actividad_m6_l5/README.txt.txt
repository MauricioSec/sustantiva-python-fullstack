====================================================================
PROYECTO: seguridad_acceso_django
AUTOR: Mauricio Monsálvez
ACTIVIDAD: Módulo 6 - Actividad N°5
====================================================================

DESCRIPCIÓN DE LA IMPLEMENTACIÓN
Este proyecto implementa un sistema de control de acceso y autorización
utilizando el framework de seguridad nativo django.contrib.auth.

CONCEPTOS APLICADOS:
1. Control de accesos y redireccionamiento: Se definieron las variables
   LOGIN_URL, LOGIN_REDIRECT_URL y LOGOUT_REDIRECT_URL en settings.py
   para gestionar el flujo de navegación y redirigir el tráfico no autorizado.

2. Tablas del modelo Auth: Se implementaron las tablas estándar (User,
   Group, Permission) integradas mediante las migraciones iniciales.

3. Manejo de sesiones: Se utilizó la plantilla de autenticación predeterminada
   por el framework en el directorio 'registration/login.html' para procesar
   el modelo Login/Logout.

4. Restricción en Vistas Basadas en Clases (CBV):
   - LoginRequiredMixin: Aplicado a la vista 'PanelPrivadoView' para denegar
     el acceso a visitantes anónimos.
     
   - PermissionRequiredMixin: Aplicado a la vista 'PanelAvanzadoView' para
     bloquear el acceso a usuarios autenticados que no posean el permiso
     requerido en la base de datos (retornando HTTP 403).

INSTRUCCIONES DE EJECUCIÓN
1. Activar el entorno virtual.
2. Iniciar el servidor de desarrollo: python manage.py runserver
3. Navegar a: http://127.0.0.1:8000/

CREDENCIALES DE AUDITORÍA (Base de datos incluida en la entrega)

- Usuario Administrador (Valida acceso total):
  Usuario: maury
  Contraseña: maury1234

- Usuario Estándar (Valida acceso a Panel Privado y bloqueo en Panel Avanzado):
  Usuario: operador
  Contraseña: oper1234
====================================================================