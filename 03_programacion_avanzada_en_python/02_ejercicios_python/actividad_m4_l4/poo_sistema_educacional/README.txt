=========================================================
SISTEMA DE GESTIÓN EDUCACIONAL - IMPLEMENTACIÓN POO
=========================================================

El presente directorio "poo_sistema_educacional" contiene el código fuente en Python que materializa el modelo de clases diseñado en la actividad anterior.

JUSTIFICACIÓN TÉCNICA DE REQUERIMIENTOS:
1. Implementación Estructural: Se codificaron las clases Persona, Alumno, Profesor, Curso, Asignatura y Calificacion con encapsulamiento estricto (atributos privados '__').
2. Polimorfismo: Implementado mediante el método `mostrar_datos()`. La clase base lo define, y las subclases (Alumno y Profesor) lo sobrescriben. Al iterar sobre una lista de Personas, el intérprete resuelve dinámicamente qué versión ejecutar según la naturaleza de la instancia.
3. Sobrecarga de métodos: Dado que Python no admite sobrecarga nativa de métodos por diseño del lenguaje, se procedió a simular este comportamiento en el método `agregar_alumno()` de la clase `Curso`, utilizando argumentos por defecto. Esto permite procesar la inyección de la dependencia de múltiples formas.
4. Interacción: El bloque "if __name__ == '__main__':" demuestra el paso de mensajes entre objetos independientes, como profesores siendo asignados a una instancia de la clase Asignatura.
=========================================================