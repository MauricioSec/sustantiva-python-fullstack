-- 1. Insertar 5 usuarios (1 administrador)
INSERT INTO usuarios (nombre, email, es_admin) VALUES
('Mauricio Monsálvez', 'admin@ecommerce.cl', TRUE),
('Juan Pérez', 'juan@correo.cl', FALSE),
('María Silva', 'maria@correo.cl', FALSE),
('Carlos López', 'carlos@correo.cl', FALSE),
('Ana Torres', 'ana@correo.cl', FALSE);

-- 2. Insertar 3 categorías
INSERT INTO categorias (nombre) VALUES
('Electrónica'), ('Ropa'), ('Hogar');

-- 3. Insertar 10 productos
INSERT INTO productos (nombre, precio, categoria_id) VALUES
('Laptop Pro', 1200000, 1),
('Smartphone X', 800000, 1),
('Auriculares Bluetooth', 150000, 1),
('Monitor 27"', 250000, 1),
('Polera Básica', 15000, 2),
('Pantalón Denim', 35000, 2),
('Chaqueta Impermeable', 60000, 2),
('Sofá Seccional', 450000, 3),
('Mesa de Centro', 85000, 3),
('Lámpara de Pie', 45000, 3);

-- 4. Insertar información de stock para cada producto
INSERT INTO stock_productos (producto_id, cantidad) VALUES
(1, 10), (2, 15), (3, 50), (4, 3), -- Stock bajo en ID 4
(5, 100), (6, 80), (7, 20),
(8, 2), (9, 5), (10, 12);          -- Stock bajo en ID 8

-- 5. Insertar 3 pedidos
INSERT INTO pedidos (usuario_id, total) VALUES
(2, 1350000),
(3, 70000),
(4, 450000);

-- 6. Insertar ítems en el detalle de pedidos
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario) VALUES
(1, 1, 1, 1200000),
(1, 3, 1, 150000),
(2, 6, 2, 35000),
(3, 8, 1, 450000);