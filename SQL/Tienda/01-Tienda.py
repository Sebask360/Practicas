import mysql.connector

#--- Generamos una conexión 
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="09022004"
)

miCursor = conexion.cursor()

#--- Creamos la base de datos si no existe
miCursor.execute("CREATE DATABASE IF NOT EXISTS Tienda")
conexion.commit()

#--- Accedemos a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="09022004",
    database="Tienda"
)

miCursor = conexion.cursor()

#---Creamos una tabla llamada Productos, que tiene un id de producto de tipo entero, auto incrementable, y su primary kay ; un nombre de tipo varchar de 255 y no nulo, y un precio decimal de una longitud de 10, y con dos decimales.
miCursor.execute("""
    CREATE TABLE IF NOT EXISTS Productos(
        id_producto INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        precio DECIMAL(10,2) NOT NULL
    )
""")

#--- Creamos una tabla llamada ventas, con una columna para el id de ventam, que va a ser de tipo entero, auto incrementable, y va a ser su primary key, un id de producto que va a ser una clave foranea que hace referencia al id de un producto de la tabla Productos; cantidad vendida que va a ser de tipo entero y no va a ser nula, y fecha de venta que va a ser de tipo DATE y tambien va a ser no nula. 
miCursor.execute("""
    CREATE TABLE IF NOT EXISTS Ventas(
        id_venta INT AUTO_INCREMENT PRIMARY KEY,
        id_producto INT,
        cantidad_vendida INT NOT NULL,
        fecha_venta DATE NOT NULL,
        FOREIGN KEY (id_producto) REFERENCES Productos(id_producto) ON DELETE CASCADE
    )
""")

#--- Insertamos datos en la tabla Productos, insertamos un nnombre y precio, 4 veces. 
miCursor.execute("""
    INSERT INTO Productos (nombre, precio)
    VALUES ('Azúcar', 15.25),
           ('Café', 6.25),
           ('Pan', 9.99),
           ('Masmelos', 19.25)
""")
conexion.commit()

#--- Insertamos datos en la tabla Ventas
miCursor.execute("""
    INSERT INTO Ventas (id_producto, cantidad_vendida, fecha_venta)
    VALUES (1, 2, '2024-09-15')
""")
conexion.commit()

#--- Cerramos la conexión a la base de datos y el cursor
miCursor.close()
conexion.close()
