
-- Crear base de datos
CREATE DATABASE SistemaVentas2;

-- Usar la base de datos que se creo
USE SistemaVentas2;

-- Crear tabla Productos

CREATE TABLE Productos (
	id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    fecha_ingreso DATE
);

-- Crear tabla Clientes

CREATE TABLE Clientes (
	id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre_cliente VARCHAR(100) NOT NULL,
    email_cliente VARCHAR(100) NOT NULL
);

-- Crear tabla Ordenes

CREATE TABLE Ordenes (
	id_orden INT AUTO_INCREMENT PRIMARY KEY,
    fecha_orden DATE,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente) ON DELETE CASCADE
);

-- Crear tabla Detalle_Ordenes

CREATE TABLE Detalle_Ordenes (
	id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_orden INT,
    id_producto INT,
    cantidad INT,
    FOREIGN KEY (id_orden) REFERENCES Ordenes(id_orden) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto) ON DELETE CASCADE
);



-- Insertar productos 

INSERT INTO Productos (nombre_producto, precio, fecha_ingreso)
VALUES  ('Producto A', 25.50, '2024-09-01'),
		('Producto B', 15.00, '2024-08-15'),
        ('Producto C', 60.75, '2024-09-05'),
        ('Producto D', 45.00, '2024-07-09'),
        ('Producto E', 85.00, '2024-06-30');


SELECT * FROM Productos;

-- Insertar clientes

INSERT INTO Clientes (nombre_cliente, email_cliente)
VALUES  ('Juan Perez','juan.perez@gmail.com'),
		('Ana Garcia','ana.garcia@gmail.com'),
        ('Luis Lopez','luis.lopez@gmail.com');
        
SELECT * FROM Clientes;        

-- Insertar Ordenes

INSERT INTO Ordenes (fecha_orden, id_cliente)
VALUES ('2024-09-06', 1),
	   ('2024-09-06', 2);

SELECT * FROM Ordenes;

-- Insertar Detalle ordenes

INSERT INTO Detalle_Ordenes (id_orden, id_producto, cantidad)
VALUES  (1, 1, 2),
		(1, 3, 1),
        (2, 2, 3),
		(2, 4, 1);

SELECT * FROM Detalle_Ordenes;

-- Consultas

SELECT P.nombre_producto, D.cantidad, C.nombre_cliente
FROM Detalle_Ordenes D
JOIN Productos P ON P.id_producto = D.id_producto
JOIN Ordenes O ON O.id_orden = D.id_orden
JOIN Clientes C ON C.id_cliente = O.id_cliente
WHERE C.nombre_cliente = 'Juan Perez';

SELECT * 
FROM Ordenes
WHERE fecha_orden >= DATE_SUB(curdate(), INTERVAL 1 MONTH);

INSERT INTO Ordenes (fecha_orden, id_cliente)
VALUES ('2024-07-06', 1),
	   ('2024-06-06', 2);


SELECT P.precio, C.nombre_cliente 
FROM Detalle_ordenes D
JOIN Productos P ON P.id_producto = D.id_producto
JOIN Ordenes O ON O.id_orden = D.id_orden
JOIN Clientes C ON C.id_cliente = O.id_cliente
WHERE P.precio > 50;

-- Actualizaciones 

UPDATE Clientes
SET email_cliente = 'nuevoemail@example.com'
WHERE id_cliente = 2;

DELETE FROM Productos
WHERE id_producto = 3;

DELETE FROM Clientes
WHERE id_cliente = 1;


CREATE DATABASE IF NOT exists
	


