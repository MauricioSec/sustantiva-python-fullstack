-- Creación de tabla Estudiantes (Entidad fuerte)
CREATE TABLE estudiantes (
    rut VARCHAR(12) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL
);

-- Creación de tabla Cursos (Entidad fuerte)
CREATE TABLE cursos (
    codigo VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    docente_responsable VARCHAR(100) NOT NULL
);

-- Creación de tabla asociativa Matriculas (Resuelve la relación N:M)
CREATE TABLE matriculas (
    estudiante_rut VARCHAR(12),
    curso_codigo VARCHAR(20),
    fecha DATE NOT NULL,
    anio INTEGER NOT NULL,
    PRIMARY KEY (estudiante_rut, curso_codigo),
    FOREIGN KEY (estudiante_rut) REFERENCES estudiantes(rut),
    FOREIGN KEY (curso_codigo) REFERENCES cursos(codigo)
);