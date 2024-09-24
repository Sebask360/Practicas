# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "09022004",
#     database = "testdb"
# )

# myCursor = mydb.cursor()

#Crear base de datos "testdb"
#myCursor.execute("CREATE DATABASE testdb ")

#Crear tabla llamada users, que tiene columnas como. nombre email, y edad. 
# myCursor.execute("CREATE TABLE users ( id_user INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), age INT)");

# sentenciaSql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
#datos = ("Santiago", "email@example.com", 89)
# myCursor.execute(sentenciaSql, datos)

#Insertamos varios datos. una lista de tuplas. y lo ejecutamos con "executemany" cuando son varios datos.
# datos = [("Axel", "axel@gmail.com", 15),
#          ("Diana","michi@gmail.com", 25),
#          ("Carlos","bombonasesino@hotmail.com", 35),
#          ("Daniel","Daniel@gmail.com", 43),
#          ("Cristobal","conquistador@gmail.com", 33)
#          ]

# myCursor.executemany(sentenciaSql, datos)
# mydb.commit()

#Select en bases de datos. 

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "09022004",
    database = "testdb"
)

# myCursor = mydb.cursor()
# myCursor.execute("SELECT * FROM users")

# resultado = myCursor.fetchall()
# for row in resultado:
#     print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")

# resultado = myCursor.fetchall()
# print("Name\t\t\tEmail\t\t\tAge\tId")
# print("----\t\t\t----\t\t\t---\t--")

# for row in resultado:
#     print(f"{row[1]}\t\t{row[2]}\t\t{row[3]}")

#----WHERE

# myCursor = mydb.cursor()
# myCursor.execute("SELECT * FROM users WHERE id_user = 1")
# resultado = myCursor.fetchall()
# # print("Name\t\t\tEmail\t\t\tAge\tId")
# # print("----\t\t\t----\t\t\t---\t--")

# for row in resultado:
#     print(row)

myCursor = mydb.cursor()

# my_sql = "UPDATE users SET email = 'Mrstark@gmail.com' WHERE id_user = 1"
# myCursor.execute(my_sql)
# mydb.commit()

my_sql = "DELETE FROM users WHERE id_user = 6"
myCursor.execute(my_sql)
mydb.commit()