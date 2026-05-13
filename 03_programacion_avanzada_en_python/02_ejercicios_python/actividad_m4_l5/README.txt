=========================================================
ENTREGABLE: CAPTURA Y CONTROL DE ERRORES EN PYTHON
=========================================================

1. ¿Qué tipo de error crees que es más común en programas reales?
En entornos de producción, los errores más comunes son de dos categorías: 
- Errores de validación de entrada (ValueError, TypeError), ocasionados por usuarios que inyectan datos con formatos inesperados o maliciosos.
- Errores de Entrada/Salida e infraestructura (IOError, ConnectionError, TimeoutError), generados cuando el sistema interactúa con bases de datos, APIs externas o sistemas de archivos que pierden conectividad o deniegan accesos.

2. ¿Por qué es importante manejar excepciones?
Es fundamental por tres razones arquitectónicas y de ciberseguridad:
- Resiliencia: Evita el colapso abrupto ("crash") del sistema operativo o del servicio ante un comportamiento anómalo.
- Integridad de Recursos: Garantiza mediante el bloque 'finally' que los puertos, conexiones de red o archivos en memoria sean liberados y cerrados correctamente, evitando fugas de memoria o corrupción de datos.
- Auditoría y Seguridad: Permite registrar el fallo exacto en los logs (bitácoras) sin revelar la traza completa (stacktrace) al usuario final, lo cual podría exponer vulnerabilidades de la arquitectura.