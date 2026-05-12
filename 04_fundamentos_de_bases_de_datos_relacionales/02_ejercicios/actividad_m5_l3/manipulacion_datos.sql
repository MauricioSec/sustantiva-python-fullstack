-- ==========================================
-- 1. Inserción de datos (INSERT)
-- ==========================================

-- Insertar al menos 3 nuevos clientes
INSERT INTO clientes (nombre, ciudad) VALUES
('Empresa Alfa', 'Santiago'),
('Transportes Beta', 'Valparaíso'),
('Naviera Gamma', 'Puerto Montt');

-- Insertar al menos 5 pedidos asociados a los clientes
-- Asumiendo que los IDs generados arriba son 1, 2 y 3.
INSERT INTO pedidos (cliente_id, fecha, total) VALUES
(1, '2026-05-10', 150000),
(1, '2026-05-11', 85000),
(2, '2026-05-12', 200000),
(3, '2026-05-13', 120000),
(2, '2026-05-14', 95000);

-- ==========================================
-- 2. Actualización de datos (UPDATE)
-- ==========================================

-- Cambiar la ciudad de un cliente con id = 2 a "Viña del Mar"
UPDATE clientes
SET ciudad = 'Viña del Mar'
WHERE id = 2;

-- Modificar el total de un pedido existente
UPDATE pedidos
SET total = 160000
WHERE id = 1;

-- ==========================================
-- 3. Eliminación de datos (DELETE)
-- ==========================================

-- Eliminar un pedido por su id
DELETE FROM pedidos
WHERE id = 5;

-- Intentar eliminar un cliente que tiene pedidos asociados
-- RESULTADO DOCUMENTADO: Esta consulta fallará.
-- El motor SQL lanzará un error de violación de Foreign Key porque la tabla
-- 'pedidos' depende de la existencia de este registro en 'clientes'.
-- Se deja comentada para no romper la ejecución del script.

-- DELETE FROM clientes WHERE id = 1;