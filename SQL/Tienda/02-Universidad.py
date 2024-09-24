import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="09022004"
)

miCursor = conexion.cursor()

miCursor.execute("CREATE DATABASE IF NOT EXISTS Universidad")
conexion.commit()

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="09022004",
    database="Universidad"
)

miCursor = conexion.cursor()

miCursor.execute("""
    CREATE TABLE IF NOT EXISTS Estudiantes(
        id_estudiate INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        apellido VARCHAR(255) NOT NULL,
        edad INT NOT NULL
    )
""")

miCursor.execute("""
    CREATE TABLE IF NOT EXISTS Cursos(
        id_curso INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        creditos INT NOT NULL
    )
""")

miCursor.execute("""
    INSERT INTO Estudiantes (nombre, apellido, edad)
    VALUES  ("Santiago", "Martinez", 19),
            ("Julian", "Rivera", 16),
            ("Diana", "Bonaparte", 15)
""")
conexion.commit()

miCursor.execute("""
    INSERT INTO Cursos (nombre, creditos)
    VALUES  ("Programacion", 15),
            ("Matematicas", 20),
            ("Arquitectura", 16)
            
""")
conexion.commit()

miCursor.close()
conexion.close()
