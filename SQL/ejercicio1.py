import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin"
)

cursor = conexion.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS tienda")
conexion.commit()

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "tienda"
)

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10,2) NOT NULL
)                             
""")

cursor.execute("""
CREATE TABLE ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
)                          
""")

cursor.execute("""
INSERT INTO productos (nombre, precio) 
VALUES ('Leche', 10.99),
       ('Pan', 5.99),
       ('Azucar', 7.99)   
""")
conexion.commit()

cursor.execute("""
INSERT INTO ventas (id_producto, cantidad, fecha) 
VALUES (1, 2, '2024-09-12')  
""")
conexion.commit()

cursor.close()
conexion.close()



