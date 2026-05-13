# Diccionario de Datos y Reflexión - Lección 5

## 1. Diccionario de Datos

### Tabla: estudiantes
| Campo | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
| :--- | :--- | :--- | :--- | :--- | :--- |
| rut | VARCHAR(12) | No | Sí | No | Identificador único del estudiante. |
| nombre | VARCHAR(100) | No | No | No | Nombre completo del estudiante. |
| correo | VARCHAR(100) | No | No | No | Dirección de correo electrónico de contacto. |

### Tabla: cursos
| Campo | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
| :--- | :--- | :--- | :--- | :--- | :--- |
| codigo | VARCHAR(20) | No | Sí | No | Identificador único del curso. |
| nombre | VARCHAR(100) | No | No | No | Nombre descriptivo de la asignatura. |
| docente_responsable | VARCHAR(100) | No | No | No | Nombre del profesor a cargo del curso. |

### Tabla: matriculas
| Campo | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
| :--- | :--- | :--- | :--- | :--- | :--- |
| estudiante_rut | VARCHAR(12) | No | Sí (Compuesta) | Sí | Referencia al RUT en tabla estudiantes. |
| curso_codigo | VARCHAR(20) | No | Sí (Compuesta) | Sí | Referencia al código en tabla cursos. |
| fecha | DATE | No | No | No | Fecha exacta en la que se realizó la inscripción. |
| anio | INTEGER | No | No | No | Año académico correspondiente a la matrícula. |

---

## 2. Reflexión

* **¿Cuál fue la mayor dificultad al transformar el modelo conceptual al relacional?**
    La abstracción de la relación de "Muchos a Muchos" (N:M). En el modelo conceptual es fácil trazar una línea entre estudiante y curso, pero al pasar al modelo relacional, las bases de datos no soportan relaciones N:M directas de forma eficiente. Fue necesario comprender la exigencia lógica de crear una tercera entidad física (la tabla asociativa `matriculas`) para alojar las llaves foráneas de ambas partes y los atributos propios de ese evento (fecha y año).

* **¿Qué ventajas tiene normalizar una base de datos? ¿Y cuándo conviene desnormalizarla?**
    **Ventajas de la normalización:** Minimiza la redundancia de datos, previene anomalías de inserción, actualización y borrado, y garantiza la integridad referencial (asegurando que cada dato tenga una única fuente de verdad).
    **Cuándo conviene desnormalizar:** Es útil en entornos OLAP (Procesamiento Analítico en Línea) o bases de datos de solo lectura orientadas a reportes y *Data Warehousing*. Se aplica cuando el rendimiento de lectura es crítico y se busca evitar el alto costo computacional de ejecutar múltiples operaciones `JOIN` complejas, aceptando a cambio una redundancia controlada.