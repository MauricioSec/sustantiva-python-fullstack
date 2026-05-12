-- ==========================================
-- 1. Consultas a una sola tabla
-- ==========================================

-- Obtener todos los registros de la tabla clientes
SELECT * FROM clientes;

-- Obtener el nombre y ciudad de todos los clientes que vivan en "Valparaíso"
SELECT nombre, ciudad 
FROM clientes 
WHERE ciudad = 'Valparaíso';

-- Obtener el cliente con id=3
SELECT * FROM clientes 
WHERE id = 3;

-- Usar COUNT() para contar cuántos clientes hay en total
SELECT COUNT(*) AS total_clientes 
FROM clientes;

-- Obtener todas las ciudades distintas en las que hay clientes (DISTINCT)
SELECT DISTINCT ciudad 
FROM clientes;

-- Agrupar clientes por ciudad y contar cuántos hay en cada una
SELECT ciudad, COUNT(*) AS cantidad_clientes 
FROM clientes 
GROUP BY ciudad;


-- ==========================================
-- 2. Consultas entre varias tablas
-- ==========================================

-- Obtener todos los pedidos, incluyendo el nombre del cliente
SELECT p.id AS pedido_id, p.fecha, p.total, c.nombre AS nombre_cliente 
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.id;

-- Obtener los pedidos hechos por clientes de "Santiago"
SELECT p.* FROM pedidos p
JOIN clientes c ON p.cliente_id = c.id 
WHERE c.ciudad = 'Santiago';

-- Obtener el total de pedidos por cliente (usando GROUP BY y SUM para el monto total)
SELECT c.nombre, SUM(p.total) AS monto_total_pedidos 
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id 
GROUP BY c.id, c.nombre;

-- Usar un LEFT JOIN para listar todos los clientes y sus pedidos, incluyendo aquellos que no han hecho pedidos
SELECT c.nombre, p.id AS pedido_id, p.fecha, p.total 
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id;

-- Crear una consulta anidada que muestre los clientes cuyo total de pedidos supera los $100.000
SELECT * FROM clientes 
WHERE id IN (
    SELECT cliente_id 
    FROM pedidos 
    GROUP BY cliente_id 
    HAVING SUM(total) > 100000
);