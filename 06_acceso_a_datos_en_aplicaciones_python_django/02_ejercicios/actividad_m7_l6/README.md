# Reflexión CRUD Django

### ¿Cómo funciona el flujo completo de una operación CRUD?
El flujo MVT (Model-View-Template) opera así:
1. El usuario realiza una petición HTTP a una URL.
2. El archivo `urls.py` intercepta la ruta y ejecuta la vista asociada.
3. La vista (`views.py`) procesa la lógica: si es lectura, interroga al Modelo (`models.py`) mediante el ORM. Si es escritura (POST), valida los datos entrantes mediante `forms.py` y actualiza la base de datos.
4. Finalmente, la vista inyecta los datos procesados en una plantilla (`templates`) y retorna un documento HTML formateado al navegador del usuario.

### ¿Qué aprendiste sobre el enrutamiento y los parámetros dinámicos en URLs?
El enrutamiento permite segmentar la aplicación mediante la función `include()`, delegando la responsabilidad de las rutas a cada app de forma modular. Los parámetros dinámicos, como `<int:id>`, capturan valores directamente desde la URI (ej. `/libros/editar/3/`) y los inyectan como argumentos en la función de la vista. Esto es fundamental para identificar unívocamente sobre qué registro específico operar en la base de datos sin necesidad de peticiones redundantes.