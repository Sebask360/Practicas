import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='09022004',
        database='libreria'
    )

def agregar_libro(titulo, autor, precio):
    connection = conectar()
    cursor = connection.cursor()
    query = "INSERT INTO libros (titulo, autor, precio) VALUES (%s, %s, %s)"
    valores = (titulo, autor, precio)
    cursor.execute(query, valores)
    connection.commit()
    print("Libro agregado exitosamente")
    cursor.close()
    connection.close()
    
def mostrar_libros():
    connection = conectar()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    for libro in libros:
        print(libro)
    cursor.close()
    connection.close()

def actualizar_libros(id, nuevo_precio):
    try:
        
        connection = conectar()    
        cursor = connection.cursor()
        query = "UPDATE libros SET precio = %s WHERE id = %s"
        valores = (nuevo_precio, id)
        cursor.execute(query, valores)
        connection.commit()
        print("Libro actualizado exitosamente")
    except mysql.connector.Error as err:
        print(f"Error al actualizar el libro: {err}")
    finally:
        cursor.close()
        connection.close()
    
def eliminar_libro(id):
    connection = conectar()
    cursor = connection.cursor()
    query = "DELETE FROM libros WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("Libro eliminado exitosamente")
    cursor.close()
    connection.close()
    
# def sub_menu():
#     while True:
#         print("1. Actualizar nombre")
#         print("2. Actualizar precio")
#         print("3. Actualizar autor")
#         break 
        # elif opcion == "6":
        #     sub_menu()
    
def menu():
    while True:
        print("\n GESTION DE LIBRERIA \n")
        print("1. Agregar libro")
        print("2. Ver libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Salir \n")
        opcion = input("Selecciona una opcion: \n")
        
        if opcion == "1":
            titulo = input("\nTitulo: ")
            autor = input("Autor: ")
            precio = float(input("Precio: "))
            agregar_libro(titulo, autor ,precio)
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            id = int(input("ID del libro a actualizar: "))
            nuevo_precio = float(input("Nuevo precio: "))
            actualizar_libros(id, nuevo_precio)
        elif opcion == "4":
            id = int(input("ID del libro a eliminar: "))
            eliminar_libro(id)
        elif opcion == "5":
            break
        else:
            print("Opcion no valida, selecciona una valida alcornoque. ")

menu()
        