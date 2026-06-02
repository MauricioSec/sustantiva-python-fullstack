# Actividad M6 L4 - Formularios en Django
**Autor:** Mauricio Monsálvez

### ¿Qué aprendiste sobre el flujo entre formulario, vista y template?
El flujo obedece a un ciclo estricto de petición-respuesta HTTP bajo el patrón MVT. El *template* actúa como la interfaz de captura,
emitiendo una petición POST al servidor. La *vista* funciona como el controlador lógico: intercepta el método HTTP, inyecta los datos
brutos (`request.POST`) en la clase del *formulario* y evalúa su integridad mediante el método `is_valid()`. Si la validación falla
(ej. longitud mínima no alcanzada), la vista devuelve el flujo al *template* adjuntando los errores nativos. Si los datos son correctos,
el flujo finaliza ejecutando la acción de negocio (persistencia) y retornando un estado de éxito.

### ¿Cuál es la ventaja de usar ModelForm?
La ventaja técnica principal es la drástica reducción de código redundante (principio DRY) y el acoplamiento seguro. Un `ModelForm`
mapea automáticamente los campos de una tabla de la base de datos hacia inputs HTML, heredando implícitamente las restricciones del modelo.
Además, abstrae el proceso de persistencia mediante el método `.save()`, evitando que el desarrollador deba instanciar objetos manualmente,
asignar atributos uno por uno y llamar a la base de datos dentro de la vista.