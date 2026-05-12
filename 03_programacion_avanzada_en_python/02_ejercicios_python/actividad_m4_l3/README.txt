=========================================================
SISTEMA DE GESTIÓN EDUCACIONAL - DIAGRAMA DE CLASES UML
=========================================================

MÓDULO: Programación Avanzada en Python
ACTIVIDAD: Generando un Diagrama de Clases (Actividad N°1/N°3)

1. DESPLIEGUE DEL MODELO
El diagrama ha sido diseñado utilizando la herramienta PlantUML dentro del entorno Visual Studio Code, empleando el enfoque de "Diagrama como Código" para asegurar la precisión estructural. El modelo abstrae un sistema educativo compuesto por actores (Persona, Alumno, Profesor) y entidades académicas (Curso, Asignatura, Calificación).

2. CONCEPTOS DE POO APLICADOS
Para dar cumplimiento a los requerimientos técnicos, se implementaron los siguientes pilares:

- HERENCIA: Se utiliza una clase base 'Persona' que centraliza atributos comunes (RUT, nombre, email), permitiendo que 'Alumno' y 'Profesor' hereden estas características y se especialicen en sus propias funciones.
- ENCAPSULACIÓN Y VISIBILIDAD: Todos los atributos se han definido con visibilidad privada (-) o protegida (#). El acceso y la modificación de estos datos se realiza estrictamente a través de métodos públicos (+) de tipo getter y setter.
- AGREGACIÓN: La relación entre 'Curso' y 'Alumno' se define como una agregación (rombo hueco), indicando que los alumnos pueden existir independientemente de la vigencia de un curso específico.
- COMPOSICIÓN: La relación entre 'Asignatura' y 'Calificación' es de composición (rombo sólido), ya que una nota no posee existencia lógica si la asignatura es eliminada del registro.

3. REQUERIMIENTOS TÉCNICOS
El diagrama respeta la sintaxis estándar UML 2.0 y está preparado para ser implementado directamente en código Python siguiendo la lógica de clases y métodos proyectada.
=========================================================