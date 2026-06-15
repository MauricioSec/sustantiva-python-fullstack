# Reflexión - Actividad 5

### ¿Qué ventajas encuentras en usar el ORM frente a SQL tradicional?
1. **Seguridad:** El ORM escapa automáticamente los parámetros, mitigando drásticamente el riesgo de inyección SQL.
2. **Abstracción de la base de datos:** Permite cambiar de motor de base de datos (ej. de SQLite a PostgreSQL) sin tener que reescribir las consultas, ya que el ORM traduce el código Python a la sintaxis SQL específica del motor activo.
3. **Mantenibilidad:** El código en Python orientado a objetos es más limpio, estructurado y fácil de integrar con la lógica de negocio que las cadenas de texto SQL incrustadas.

### ¿En qué situaciones te parece útil ejecutar SQL directamente desde Django?
El SQL crudo (mediante `.raw()` o cursores) debe reservarse para casos excepcionales, tales como:
1. **Consultas de alta complejidad:** Cuando se requieren operaciones matemáticas complejas, subconsultas anidadas profundas o recursividad que el ORM no soporta de forma nativa o que se vuelven ilegibles al intentar forzarlas en el ORM.
2. **Funciones específicas del motor:** Cuando se necesita invocar procedimientos almacenados (Stored Procedures), vistas materializadas o funciones propietarias del motor de base de datos (ej. operaciones geoespaciales avanzadas no cubiertas por GeoDjango).

### ¿Qué dificultades encontraste al trabajar con consultas más avanzadas?
La principal dificultad radica en la correcta implementación de agregaciones (`aggregate`) y anotaciones (`annotate`). Mientras que en SQL tradicional la cláusula `GROUP BY` es explícita, en el ORM de Django el agrupamiento ocurre de manera implícita dependiendo de qué campos se evalúan antes de llamar a `.annotate()`, lo que puede generar consultas SQL subyacentes inesperadas si no se comprende a fondo cómo el ORM estructura la sentencia.