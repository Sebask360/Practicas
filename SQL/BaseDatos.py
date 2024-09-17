import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "09022004",
    database = "testdb"
)

myCursor = mydb.cursor()

#Crear base de datos "testdb"
#myCursor.execute("CREATE DATABASE testdb ")

#Crear tabla llamada users, que tiene columnas como. nombre email, y edad. 
# myCursor.execute("CREATE TABLE users ( id_user INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), age INT)");

sentenciaSql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
#datos = ("Santiago", "email@example.com", 89)
# myCursor.execute(sentenciaSql, datos)

#Insertamos varios datos. una lista de tuplas. y lo ejecutamos con "executemany" cuando son varios datos.
datos = [("Axel", "axel@gmail.com", 15),
         ("Diana","michi@gmail.com", 25),
         ("Carlos","bombonasesino@hotmail.com", 35),
         ("Daniel","Daniel@gmail.com", 43),
         ("Cristobal","conquistador@gmail.com", 33)
         ]

myCursor.executemany(sentenciaSql, datos)
mydb.commit()
