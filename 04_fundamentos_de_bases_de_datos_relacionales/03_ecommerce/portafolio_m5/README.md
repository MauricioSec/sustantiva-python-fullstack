# Base de Datos Relacional - E-Commerce (MVP)

## Descripción General
Este proyecto implementa el Minimum Viable Product (MVP) para la base de datos relacional de un e-commerce. Está estructurado en seis entidades principales (`usuarios`, `categorias`, `productos`, `stock_productos`, `pedidos`, `detalle_pedidos`) que permiten gestionar de manera íntegra el catálogo, inventario y flujo de compras, diferenciando perfiles administrativos de clientes regulares.

## Orden de Ejecución de los Scripts
Para desplegar la base de datos en un gestor (como PostgreSQL), los scripts deben ejecutarse en el siguiente orden estricto para no violar la integridad referencial:
1. **`schema.sql`**: Construye las tablas y sus relaciones estructurales (DDL).
2. **`seed.sql`**: Inyecta los datos de prueba iniciales (DML).
3. **`transaction.sql`**: Ejecuta la prueba de concurrencia y actualización atómica de stock.
4. **`queries.sql`**: Scripts de consulta de información (DQL).
