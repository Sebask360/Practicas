#Practica Loop For 1
alumnos_clase = ["Maria","Jose","Carlos","Martina","Isabel","Tomas","Daniela"]

for alumno in alumnos_clase:
    print(f"Hola {alumno}")

#Practica Loop For 2
lista_numeros =[1,5,8,7,6,8,2,5,6,4,8,5,9,8,3,5,4,2,5,6,4]

suma_numeros = 0
for numero in lista_numeros:
    suma_numeros += numero

print(suma_numeros)

#Practica Loop For 3
lista_numeros =[1,5,8,7,6,8,2,5,6,4,8,5,9,8,3,5,4,2,5,6,4]

suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero %2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print(suma_impares)
print(suma_pares)

#Practica Loop While 1
numero = 10

while numero >= 0:
    print(numero)
    numero -= 1

# Practica Loop While 2
numero = 50

while numero >= 0:
    if numero %5 == 0:
        print(numero)
    numero -= 1

#Practica Interrupcion de Flujo
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4, 3]

for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)

#Practica de Rango 1
mi_lista = (list(range(2500, 2586,1)))

print(mi_lista)

#Practica de Rango 2
mi_lista = (list(range(3,301,3)))
print(mi_lista)

#Practica de Rango 3
suma_cuadrados = 0

for numero in range(1,16,1):
    cuadrado = numero **2
    suma_cuadrados += cuadrado
    print(suma_cuadrados) 