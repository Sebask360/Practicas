class Juguete:
    def __init__(self,nombre,categoria,precio,cantidad):
        self.nombre = nombre 
        self.cateforia = categoria
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - {self.cateforia} -  ${self.precio} - {self.cantidad} en Stock"
    
    def actualizarCantidad(self, cantidad):
        self.cantidad = cantidad

class AlmacenJuguete:
    def __init__(self):
        self.inventario = []

    def agregarJuguete(self, juguete):
        self.inventario.append(Juguete)
        
    def eliminarJuguete(self, nombre):
        self.inventario = [juguete for juguete in self.inventario if juguete.nombre != nombre]
    
    def listarJuguete(self):
        if not self.inventario:
            print("No hay juguetes en Stock. ")
        else:
            for juguete in self.inventario:
                print(juguete)
    def encontrarJuguete(self, nombre):
        for  juguete in self.inventario:
            if juguete.nombre == nombre:
                return juguete
        return None
    
    def actualizarCantidadJuguete(self, nombre, cantidad):         
        juguete = self.encontrarJuguete(nombre)
        if juguete:
            juguete.actualizarCantidad(cantidad)
        else:
            print(f"Juguete {nombre} no encontrado. ")
            
def mostrarMenu():
    print("MENU DEL ALMACEN DE JUGUETES")
    print("1. Agregar Juguete")
    print("2. Eliminar Juguete")
    print("3. Listar Juguete")
    print("4. Encontrar Juguete")
    print("5. Actualizar la cantidad de Juguetes")
    print("6. Salir")

def main(): 
    almacen = AlmacenJuguete()
    while True:
        mostrarMenu()
        opcion = int(input("Ingrese la opcion: "))
        
        if opcion == 1:
            nombre = input("Ingrese el nombre del juguete: ")
            categoria = input("Ingrese la categoria del juguete: ")
            precio = float(input("Ingrese el precio del juguete: "))
            cantidad = int(input("Ingrese la cantidad del juguete: "))
            juguete = Juguete(nombre, categoria, precio, cantidad)
            almacen.agregarJuguete(juguete) 