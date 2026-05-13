BEGIN;

-- 1. Creación de un nuevo pedido para el usuario 5
INSERT INTO pedidos (id, usuario_id, fecha, total) 
VALUES (4, 5, CURRENT_TIMESTAMP, 1600000);

-- 2. Registro de productos comprados (2 unidades del producto 2)
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario) 
VALUES (4, 2, 2, 800000);

-- 3. Actualización del stock correspondiente (Restar 2 unidades)
UPDATE stock_productos 
SET cantidad = cantidad - 2 
WHERE producto_id = 2;

COMMIT;