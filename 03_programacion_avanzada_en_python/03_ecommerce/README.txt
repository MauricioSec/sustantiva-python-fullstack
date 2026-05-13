=========================================================
ECOMMERCE CLI - POO, ROLES Y PERSISTENCIA
=========================================================

1. Descripción general
Esta aplicación es un sistema de comercio electrónico de consola desarrollado puramente en Python mediante el Paradigma Orientado a Objetos (POO). Implementa una separación estricta de responsabilidades a través de herencia, definiendo dos actores principales: Administradores (gestión de inventario) y Clientes (operaciones de compra). La persistencia de datos se asegura mediante la manipulación de archivos de texto plano.

2. Instrucciones de ejecución
- Requiere tener instalado Python 3.x.
- Abrir una terminal o línea de comandos.
- Navegar hasta el directorio donde se encuentra el archivo.
- Ejecutar el comando: python main.py

3. Arquitectura técnica implementada
- Clases y Herencia: Las clases Admin y Cliente heredan los atributos base de la clase padre Usuario.
- Composición: La clase Cliente instancia y posee un objeto Carrito. La clase Catalogo aloja múltiples instancias de Producto.
- Excepciones: Se implementaron clases de excepción personalizadas (ProductoNoEncontradoError, CantidadInvalidaError) para proteger las reglas de negocio, además de la captura de errores estándar (IOError, ValueError).
- Archivos: El catálogo se carga/escribe en 'catalogo.txt' y las transacciones finalizadas se apendan a 'ordenes.txt'.