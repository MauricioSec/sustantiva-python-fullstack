# Respuestas: Transacciones en SQL

## ¿Qué es una transacción en bases de datos y por qué es importante?
Una transacción es una unidad lógica de procesamiento que agrupa una o más operaciones SQL. Es importante porque garantiza que la base de datos pase de un estado consistente a otro. Si alguna de las operaciones dentro de la transacción falla, ninguna se aplica, previniendo la corrupción de datos y manteniendo la integridad de la información.

## Propiedades ACID
* **Atomicidad:** Todo o nada. Las operaciones de una transacción se ejecutan por completo, o no se ejecuta ninguna.
* **Consistencia:** Una transacción solo puede llevar la base de datos de un estado válido a otro, respetando todas las reglas y restricciones (como las claves foráneas).
* **Aislamiento:** Las transacciones concurrentes no interfieren entre sí. El resultado de ejecutarlas en paralelo es el mismo que si se ejecutaran en serie.
* **Durabilidad:** Una vez que la transacción se confirma (COMMIT), los cambios son permanentes y sobreviven a fallos del sistema.

## Documentación del Ejercicio Práctico

### Ejercicio 1: Uso de ROLLBACK
```sql
BEGIN;
UPDATE pedidos SET total = 0 WHERE id = 1;
ROLLBACK;