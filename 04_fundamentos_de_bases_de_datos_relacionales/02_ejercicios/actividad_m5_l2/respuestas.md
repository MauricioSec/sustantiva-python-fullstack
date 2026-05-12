# Respuestas Teóricas - Actividad 2

## ¿Qué es un modelo de datos y para qué sirve en bases relacionales?
Un modelo de datos es una representación lógica y abstracta que define cómo se estructura, organiza y almacena la información dentro de un sistema. En las bases de datos relacionales, sirve para establecer las entidades (tablas), sus atributos (columnas) y las reglas de negocio (relaciones y restricciones). Su propósito fundamental es garantizar la consistencia de la información, reducir la redundancia y asegurar que el diseño soporte de manera eficiente las operaciones de la organización antes de la implementación física.

## ¿Qué es una clave foránea y qué garantiza?
Una clave foránea (Foreign Key) es una columna o un conjunto de columnas en una tabla que hace referencia a la clave primaria (Primary Key) de otra tabla. 

Garantiza la **integridad referencial** del modelo. Esto significa que impone una restricción técnica que impide registrar datos huérfanos o inconsistentes. Por ejemplo, en este ejercicio, la clave foránea garantiza que no se pueda insertar un registro en la tabla `pedidos` si el `cliente_id` no existe previamente en la tabla `clientes`.