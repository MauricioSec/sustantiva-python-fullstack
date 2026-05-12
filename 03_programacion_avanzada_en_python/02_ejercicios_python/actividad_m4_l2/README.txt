Entregable: Actividad N° 2 - Reflexión

¿Qué relación te pareció más fácil de implementar: colaboración o composición? ¿Por qué?
La colaboración resultó ser metodológicamente más fácil y limpia de implementar. Al ser una relación de uso entre objetos independientes, basta con crear el objeto "Autor" por separado en el flujo principal e inyectarlo en el constructor del "Libro". Esto mantiene las responsabilidades separadas.

Por otro lado, la composición es más rígida de implementar porque requiere acoplamiento. Obliga a que la clase "Libro" sea responsable de gestionar los parámetros (nombre_editorial y ciudad_editorial) únicamente para poder instanciar la clase "Editorial" dentro de su propio constructor. Esto aumenta la complejidad de la inicialización de la clase principal y ata el ciclo de vida de la editorial al del libro.