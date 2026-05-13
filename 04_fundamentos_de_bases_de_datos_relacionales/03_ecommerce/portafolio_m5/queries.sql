-- Listar todos los productos junto a su categoría
SELECT p.nombre AS producto, p.precio, c.nombre AS categoria
FROM productos p
JOIN categorias c ON p.categoria_id = c.id;

-- Buscar productos por nombre (Ej. que contengan 'Laptop')
SELECT * FROM productos
WHERE nombre ILIKE '%Laptop%';

-- Filtrar productos por categoría (Ej. 'Ropa')
SELECT p.nombre, p.precio
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
WHERE c.nombre = 'Ropa';

-- Mostrar los productos asociados a un pedido (Ej. Pedido ID 1)
SELECT dp.pedido_id, p.nombre, dp.cantidad, dp.precio_unitario
FROM detalle_pedidos dp
JOIN productos p ON dp.producto_id = p.id
WHERE dp.pedido_id = 1;

-- Calcular el total de un pedido de forma dinámica (Ej. Pedido ID 1)
SELECT pedido_id, SUM(cantidad * precio_unitario) AS total_calculado
FROM detalle_pedidos
WHERE pedido_id = 1
GROUP BY pedido_id;

-- Identificar productos con stock bajo (Menor estricto a 5 unidades)
SELECT p.nombre, sp.cantidad AS stock_actual
FROM productos p
JOIN stock_productos sp ON p.id = sp.producto_id
WHERE sp.cantidad < 5;