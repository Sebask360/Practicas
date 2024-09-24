class Estudiante:
    def __init__ (self, nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def __str__(self):
        return(f"Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}")
    
class Curso:
    def __init__ (self,nombre,profesor):
        self.nombre =  nombre
        self.profesor = profesor
        self.estudiantes = []
        
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado al curso {self.nombre}")
    
    def eliminar_estudiante(self,nombre_estudiante):
        
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre_estudiante:
                self.estudiantes.remove(estudiante)
                print(f"El estudiante {nombre_estudiante} ha sido eliminado del curso {self.nombre}.")
                return
        print(f"Estudiante {nombre_estudiante} no se encuentra en el curso {self.nombre}.")
    
    def mostrar_estudiantes(self):
        
        if self.estudiantes:
            print(f"Estudiantes incritos en el curso {self.nombre}")
            for estudiante in self.estudiantes:
                print(estudiante)
        else:
            print(f"No hay estudiantes incritos en el curso {self.nombre}")
            
estudiante1 = Estudiante("Sebastian", 20, "Noveno")
estudiante2 = Estudiante("Santiago",  20 , "Noveno")

curso1 = Curso("Programacion", "Notch")
curso1.agregar_estudiante(estudiante1)
curso1.agregar_estudiante(estudiante2)

curso1.mostrar_estudiantes()
curso1.eliminar_estudiante('Santiago')
curso1.mostrar_estudiantes()
