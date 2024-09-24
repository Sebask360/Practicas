condicion = 0
hacer_algo = 1
hacer_otra_cosa = 2
lista = [0,1,2,3]
resultado = None
argumentos = None


#--Variables 

x = 5
y = "Python"
z = True

#--Tipos de Datos

entero = 10
flotante = 3.1416
cadena = "Hola mundo"
booleano = False

#--if-else

condicion = 0
hacer_algo = 1
hacer_otra_cosa = 2
if condicion:
    hacer_algo
else:
    hacer_otra_cosa
    
#--foor loop 

for elementos in lista:
    hacer_algo
    
#-- While loop

while condicion:
    hacer_algo

#-- Definir una funcion

def nombre_funncion(parametros):
    hacer_algo
    return resultado

#-- Llamar una funcion 

nombre_funncion(argumentos)

#-- Lista 

mi_lista = [1,2,3,4,5,6]

#-- Acceder a elementos de la lista 

primer_elemento = mi_lista[0]
ultimo_elemento = mi_lista[-1]

#-- Tuplas 

tupla = (1,2,3)

#-- Dicionarios 

mi_diccionario = {"clave1": "valor 1", "clave2" : "valor 2"}

#-- Acceder a elementos del diccionario 

valor = mi_diccionario["clave1"]   

#-- Operaciones
# Suma

suma = 1 + 2

# Resta 

resta = 2 - 1

# Multiplicacion

multiplicacion = 3 * 2

# Division 

division = 100/10

# Modulo 

modulo = 10%3

# Potencia    

2**3

#-- Concatenacion 

cadena_concatenada = "Hola" + " " + "Mundo"

#-- Longitud de una Cadena

longitud = len("Python")

#-- Conversion a mayusculas

mayusculas = "python".upper()

#-- Conversion a minusculas

minusculas = "PYTHON".lower()

#-- Impresion
# Impresion basica

print(valor)

# Imprimir tipos de datos 

print(type(valor))

#-- Entrada por consola 

valor = input("Ingresa un valor: ")

#-- Conversion de datos.
# Flotante a entero 

int(flotante)

# Entero a flotante

float(entero)

#-- Caracteres especiales 

tabulador = "tabulador\t"

tabulador_vertical = "Tabulador vertical\v"

salto_de_linea = "salto de linea\n"

barra_invertida = "Imprime una barra invertida \\"

comillas = "Imprime comillas \"" + "Tambien sirve con comillas simples\'"

retroceso = "Borra caracter anterior\b"

#-- Clases 

class Persona:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = "nombre"
        self.atributo2 = "edad"
persona = Persona("Sebastian", 20)

#-- Importar modulos 

import math

numero_pi = math.pi #3.14159...


print(numero_pi)