class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False
    
    def marcarTarea(self):
        self.estado = True
    def __str__(self):
        estado = "Completada" if self.estado else "Pendiente"
        return(f"La tarea: {self.nombre} esta {self.estado}")

class ListaTareas:
    def __init__(self):
        self.tareas = []
        
    def agregarTarea(self, nombre):
        nuevaTarea = Tarea(nombre)
        self.tareas.append(nuevaTarea)
        
    def marcarTarea(self, indice):
            self.tareas[indice].marcarTarea()
            
    def encontrarTarea(self):
        if not self.tareas:
            print("Mp hay tareas en la lista. ")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i+1}. {tarea}")
        
def mostrarMenu():
    listaTareas = ListaTareas()
    



def main():
    while True:
        print("MENU DEL GESTOR DE TAREAS")
        print("1. Agregar Tarea")
        print("2. Mostrar todas las tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")
    
        opcion = int(input("Elija una opcion. "))
    
        if opcion == 1:
            nombre = input("Ingrese la tarea pendiente")

        elif opcion == 2:
            listaTareas.encontarTareas()
        
        elif opcion == 3:
            listaTareas.marcarTarea(self.estado)
            
            

main()
    