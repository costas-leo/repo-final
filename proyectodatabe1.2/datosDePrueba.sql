-- Usar la base de datos inventario
USE inventario;

-- Insertar datos en la tabla "categorias"
INSERT INTO categorias (nombre, descripcion) VALUES
('Electrónica', 'Dispositivos electrónicos como celulares y computadoras'),
('Hogar', 'Artículos para el hogar como muebles y electrodomésticos'),
('Ropa', 'Prendas de vestir para hombres, mujeres y niños');

--Insertar datos en la tabla "productos"
INSERT INTO productos (nombre, descripcion, precio, stock, categoria_id) VALUES
('Laptop HP', 'Laptop HP con 16GB RAM y 512GB SSD', 1200.50, 50, 1),  -- categoría_id = Electrónica
('Televisor LG', 'Smart TV de 55 pulgadas', 800.00, 30, 1),           -- categoría_id = Electrónica
('Sofá', 'Sofá de tres plazas, color gris', 500.00, 20, 2),          -- categoría_id = Hogar
('Camiseta', 'Camiseta de algodón, talla M', 15.00, 100, 3);         -- categoría_id = Ropa

-- Insertar datos en la tabla "importadores"
INSERT INTO importadores (nombre, direccion, telefono, email) VALUES
('ABC Importaciones', 'Calle Falsa 123', '123456789', 'abc@importador.com'),
('Global Trade Co.', 'Av. Siempre Viva 742', '987654321', 'global@trade.com');

-- Insertar datos en la tabla "producto_importador"
INSERT INTO producto_importador (producto_id, importador_id, fecha_importacion) VALUES
(1, 1, '2025-01-10 10:00:00'), -- Laptop HP importada por ABC Importaciones
(2, 1, '2025-01-11 14:30:00'), -- Televisor LG importado por ABC Importaciones
(3, 2, '2025-01-09 08:15:00'); -- Sofá importado por Global Trade Co.

-- Insertar datos en la tabla "movimientos"
INSERT INTO movimientos (producto_id, tipo, cantidad, fecha, observaciones) VALUES
(1, 'entrada', 10, '2025-01-12 09:00:00', 'Nueva remesa de laptops'),
(2, 'entrada', 5, '2025-01-12 10:00:00', 'Televisores adicionales para promoción'),
(3, 'salida', 2, '2025-01-12 11:00:00', 'Venta a cliente particular');
