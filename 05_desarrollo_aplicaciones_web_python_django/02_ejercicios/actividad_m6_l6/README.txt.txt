Proyecto: Levantamiento y Gestión del Sistema Administrativo de Django
Autor: Mauricio Monsálvez

Descripción General:
El presente proyecto implementa y documenta el levantamiento del módulo de administración nativo de Django, enfocado en el control de acceso y la seguridad del sistema mediante la gestión estructurada de usuarios, grupos y permisos (RBAC).

Detalles de Implementación y Conceptos Aplicados:

1. Creación del Superusuario:
   - Se generó un superusuario administrador a través de la interfaz de línea de comandos (CLI) utilizando 'python manage.py createsuperuser' para garantizar el acceso raíz inicial al panel administrativo.

2. Gestión de Grupos y Permisos (Aplicación del Principio de Menor Privilegio):
   Para evitar la asignación de privilegios excesivos, se segregaron las funciones creando roles específicos desde el panel administrativo:
   - Grupo "Administración": Configurado con permisos operativos granulares y restringidos (ej. capacidad de ver y modificar usuarios o grupos), eliminando permisos destructivos totales.
   - Grupo "Auditores": Configurado bajo un modelo de solo lectura, con permisos exclusivos de visualización (ej. view_user, view_log_entry), permitiendo la inspección sin capacidad de alteración.

3. Gestión de Usuarios y Herencia:
   - Se registraron usuarios estándar en la base de datos de Auth nativa.
   - La asignación de permisos se centralizó en los grupos. Los usuarios individuales heredan los accesos de sus grupos respectivos, eliminando la redundancia de permisos directos a nivel de usuario individual para mantener una arquitectura de seguridad limpia y auditable.

Instrucciones de Ejecución:
1. Activar el entorno virtual del proyecto (env\Scripts\activate).
2. Ejecutar el servidor de desarrollo: python manage.py runserver.
3. Ingresar a la ruta http://127.0.0.1:8000/admin/

Credenciales de Evaluación (Entorno Local):

- Rol: Superusuario (Acceso Total)
  Usuario: Admin
  Contraseña: admin1234

- Rol: Operador (Grupo Administración - Permisos Restringidos)
  Usuario: Mauricio
  Contraseña: mau12345

- Rol: Auditor (Grupo Auditores - Solo Lectura)
  Usuario: Auditor
  Contraseña: audi1234