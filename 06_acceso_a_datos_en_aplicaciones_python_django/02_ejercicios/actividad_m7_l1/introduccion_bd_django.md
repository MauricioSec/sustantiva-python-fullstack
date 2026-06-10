# Actividad N° 1 – Introducción al Acceso a Bases de Datos con Django

## 1. Bases de datos en Django

* **¿Qué función cumple una base de datos dentro de una aplicación Django?**
    La función principal es la persistencia de datos. Se encarga de almacenar, recuperar, modificar y eliminar la información dinámica de la aplicación (como usuarios, registros, transacciones) de manera estructurada y segura, permitiendo que la información sobreviva a los reinicios del servidor.

* **¿Qué sistemas de bases de datos relacionales soporta Django por defecto?**
    Django incluye soporte oficial integrado para PostgreSQL, MariaDB/MySQL, Oracle y SQLite.

* **¿Cuál es el motor de base de datos que se utiliza por defecto al crear un nuevo proyecto? ¿Por qué crees que es ese?**
    El motor por defecto es **SQLite** (a través del archivo `db.sqlite3`). Se utiliza por defecto porque es una base de datos basada en archivos que no requiere instalación, configuración de servidores ni administración de usuarios. Esto reduce la fricción inicial y permite al desarrollador comenzar a construir y probar la aplicación inmediatamente.

## 2. ORM en Django

* **¿Qué es un ORM y cómo se diferencia de escribir sentencias SQL manualmente?**
    Un ORM (*Object-Relational Mapping*) es una capa de abstracción que convierte las tablas de una base de datos relacional en clases de Python, y los registros en instancias de esas clases. Se diferencia de escribir SQL manualmente en que el desarrollador opera sobre objetos y métodos de Python (paradigma orientado a objetos) en lugar de redactar cadenas de texto con consultas SQL. El ORM traduce automáticamente estas operaciones de Python al dialecto SQL del motor subyacente.

* **Menciona al menos dos ventajas de usar el ORM de Django.**
    1.  **Seguridad nativa:** El ORM parametriza automáticamente las consultas, lo que previene ataques de inyección SQL sin requerir intervención manual del desarrollador.
    2.  **Portabilidad (Agnosticismo de Base de Datos):** Permite cambiar el motor de base de datos (por ejemplo, de SQLite a PostgreSQL) modificando únicamente la configuración en `settings.py`, sin necesidad de reescribir las consultas, ya que el ORM se encarga de generar el SQL específico para cada motor.

* **Explica qué significa que una clase modelo en Python represente una tabla en la base de datos.**
    Significa que la definición estructural de la clase dicta el esquema de la base de datos. El nombre de la clase se convierte en el nombre de la tabla, los atributos de la clase (como `models.CharField`) se convierten en las columnas de la tabla con sus respectivos tipos de datos y restricciones, y cada objeto instanciado a partir de esa clase equivale a una fila de datos (un registro) dentro de esa tabla.

## 3. Migraciones

* **¿Qué son las migraciones en Django y por qué son importantes?**
    Las migraciones son archivos autogenerados en Python que describen los cambios realizados en los modelos (creación de tablas, adición de campos, modificaciones). Son importantes porque actúan como un sistema de control de versiones para el esquema de la base de datos, permitiendo aplicar, revertir y compartir la evolución estructural de los datos entre diferentes entornos de manera controlada y reproducible.

* **¿Qué comandos se utilizan para:**
    * **Crear una nueva migración a partir de cambios en los modelos:** `python manage.py makemigrations`
    * **Aplicar las migraciones a la base de datos:** `python manage.py migrate`

## 4. Consultas básicas con el ORM

* **a) Obtener todos los libros:**
    `Libro.objects.all()`

* **b) Filtrar los libros por autor igual a "Cervantes":**
    `Libro.objects.filter(autor="Cervantes")`

* **c) Obtener un libro específico por su id:**
    `Libro.objects.get(id=1)` *(Nota: asumiendo que se busca el id 1. También se puede usar `pk=1`).*