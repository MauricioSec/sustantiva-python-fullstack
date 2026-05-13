-- ==========================================
-- 1. Creación de tablas
-- ==========================================

CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100),
    departamento_id INTEGER,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

-- EXPLICACIONES TEÓRICAS:
-- ¿Qué es una clave primaria y por qué se usa en id?
-- R: Una clave primaria (PRIMARY KEY) es un identificador único e irrepetible para cada registro en una tabla. Se usa en el campo 'id' para asegurar que cada departamento y cada empleado puedan ser identificados de forma unívoca por el motor de la base de datos, sirviendo como punto de anclaje para vincular datos.

-- ¿Qué significa NOT NULL?
-- R: Es una restricción de integridad que impide que una columna acepte valores nulos o vacíos. Obliga a que el dato (por ejemplo, el 'nombre') sea proporcionado siempre que se inserte un nuevo registro.

-- ¿Qué relación existe entre empleados y departamentos?
-- R: Existe una relación de "Uno a Muchos" (1:N). Un departamento puede agrupar a múltiples empleados, pero un empleado pertenece a un solo departamento. Esta relación técnica se establece mediante la clave foránea 'departamento_id' en la tabla 'empleados', que apunta a la clave primaria 'id' de 'departamentos'.


-- ==========================================
-- 2. Modificar tablas existentes
-- ==========================================

-- Agregar nuevas columnas a las tablas creadas
ALTER TABLE empleados ADD COLUMN fecha_ingreso DATE;
ALTER TABLE departamentos ADD COLUMN ubicacion VARCHAR(100);

-- Modificar el campo correo de empleados para que no permita nulos
ALTER TABLE empleados ALTER COLUMN correo SET NOT NULL;

-- Intentar modificar una clave primaria y documentar qué ocurre
-- INSTRUCCIÓN A EVALUAR:
-- ALTER TABLE departamentos ALTER COLUMN id TYPE VARCHAR(50);
-- RESULTADO DOCUMENTADO: 
-- Si ejecutas la línea anterior, el motor SQL lanzará un error de dependencia (ej: "cannot alter type of a column used by a view or rule"). Esto ocurre porque la columna 'id' de 'departamentos' está siendo referenciada por la clave foránea de 'empleados'. El motor impide modificar la estructura de la clave primaria para proteger la integridad referencial de los datos secundarios.


-- ==========================================
-- 3. Eliminar y truncar tablas
-- ==========================================

-- Eliminar la tabla empleados
-- Se debe eliminar 'empleados' ANTES que 'departamentos', ya que 'empleados' es la tabla dependiente (hija).
DROP TABLE empleados;

-- Crear una tabla temporal de prueba, insertar registros y ejecutar TRUNCATE
CREATE TABLE tabla_prueba (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(50)
);

INSERT INTO tabla_prueba (descripcion) VALUES ('Dato de prueba 1'), ('Dato de prueba 2');

TRUNCATE TABLE tabla_prueba;

-- EXPLICACIÓN TEÓRICA:
-- Diferencia entre DELETE y TRUNCATE:
-- R: DELETE es una instrucción DML que elimina filas una por una evaluando condiciones lógicas (WHERE) y registrando cada borrado en el historial del sistema (es más lento). TRUNCATE es una instrucción DDL que vacía la tabla completa de un solo golpe liberando el espacio en disco, sin evaluar condiciones ni registrar la eliminación fila por fila (es mucho más rápido y drástico).