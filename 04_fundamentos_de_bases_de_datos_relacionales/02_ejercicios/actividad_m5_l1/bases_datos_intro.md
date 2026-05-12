# Actividad N° 1 - Rol y Componentes de una Base de Datos Relacional
**Módulo:** Fundamentos de Bases de Datos Relacionales
**Alumno:** Mauricio Monsálvez

---

## 1. El rol de una base de datos

Por lo que he aprendido en este módulo, el rol principal de una base de datos relacional dentro de una empresa es ser el "cerebro" donde se guarda toda la información importante de manera ordenada y segura. En lugar de tener los datos repartidos en archivos de Excel sueltos que se pueden perder o duplicar, la base de datos centraliza todo para que distintas aplicaciones (como las que programaremos en Python) puedan consultarla al mismo tiempo sin que el sistema colapse.

**Mis 3 ejemplos de uso serían:**
1. **Sistema de usuarios:** Para nuestra futura aplicación web, necesitamos guardar los correos, contraseñas (encriptadas) y nombres de las personas que se registran.
2. **Sistema de e-commerce / Ventas:** Para guardar el registro de qué cliente compró qué producto, cuándo lo hizo y cuánto pagó.
3. **Gestión de inventario:** Para que una bodega sepa exactamente cuántos productos le quedan en stock y le avise al sistema si falta algo.

---
 
## 2. Características de un RDBMS

Un RDBMS significa Sistema de Gestión de Bases de Datos Relacionales. Básicamente, es el software o motor (el programa en sí) que instalamos en el servidor para que se encargue de administrar nuestra base de datos.

**3 características que lo diferencian de otros sistemas (como los archivos de texto o bases NoSQL):**
1. **Usa SQL:** Todo se consulta mediante el lenguaje estructurado SQL.
2. **Integridad de los datos:** No te deja hacer cosas ilógicas, por ejemplo, no me dejaría registrar la venta de un producto a un "Cliente X" si ese cliente no existe previamente en el sistema.
3. **Estructura en tablas:** Toda la información está rígidamente estructurada en tablas (filas y columnas) que se relacionan entre sí.

**3 RDBMS muy usados en la industria:**
1. **PostgreSQL:** Es súper potente, open source y es el que más se recomienda para trabajar con Python y Django en aplicaciones grandes.
2. **MySQL:** Es un clásico, se usa muchísimo en la web tradicional, sobre todo en páginas hechas con PHP o WordPress.
3. **SQLite:** Este me llamó la atención porque viene incluido en Python. Se usa mucho para aplicaciones de celular o para hacer pruebas locales rápidas porque no requiere instalar un servidor.

---

## 3. Herramientas y objetos

Para no tener que interactuar con la base de datos a ciegas, usamos distintas herramientas:
* **Línea de comandos (CLI):** Podemos usar `psql` para escribir comandos directo en la terminal de nuestro computador.
* **Interfaz gráfica (GUI):** Herramientas como **pgAdmin 4** (que es la que instalé siguiendo el consejo del profe) o DBeaver, que nos dejan ver las tablas con botones y menús.

**Objetos principales dentro de la base de datos:**
* **Tabla:** Es la estructura básica donde realmente se guardan los datos, es parecida a una hoja de cálculo con columnas (atributos) y filas (registros).
* **Vista:** Es como guardar una consulta SQL que usamos mucho. No guarda datos nuevos, solo nos muestra la información de las tablas originales de forma más resumida o filtrada.
* **Índice:** Funciona igual que el índice de un libro. Sirve para que el motor busque la información mucho más rápido sin tener que leer toda la tabla fila por fila.
* **Llave primaria (Primary Key):** Es el identificador único de cada fila en una tabla (como el RUT de una persona o el ID de un producto). Evita que existan registros duplicados.
* **Llave foránea (Foreign Key):** Es el campo que nos permite conectar una tabla con otra. Por ejemplo, en la tabla "Ventas", guardar el ID del cliente que compró.

---

## 4. Práctica guiada (PostgreSQL + pgAdmin 4)

Para esta parte, utilicé el motor de PostgreSQL y la herramienta gráfica pgAdmin 4 que instalé para el curso. Estos fueron los pasos que seguí para crear mi primera base de datos:

1. **Conexión:** Abrí el programa pgAdmin 4 en mi computador. Me pidió la contraseña maestra que configuré al instalarlo para conectarme al servidor local (`localhost`).
2. **Crear la BD:** En el menú del lado izquierdo (Browser), busqué la carpeta "Databases". Le di clic derecho, seleccioné `Create` y luego `Database...`.
3. **Nombrar:** Se abrió una ventana, en la pestaña "General" escribí el nombre `empresa_demo` y dejé a "postgres" como dueño (owner). Luego le di al botón *Save*.
4. **Comprobar:** Listo, la base de datos `empresa_demo` apareció en mi lista. Para probar que funcionaba, le di clic derecho, abrí el `Query Tool` y ejecuté un código SQL rápido para ver que estaba todo en orden.

*(Adjunto las capturas de pantalla de este proceso en la carpeta .zip).*