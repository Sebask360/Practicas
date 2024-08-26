#Practica Random 1
import random 
aleatorio = random.randint(1,10)
print(aleatorio)

#Practica Random 2
aleatorio = random.random()
print(aleatorio)

#Practica Random 3
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = random.choice(nombres)
print(sorteo)

#Practica COmprension de Listas 1
numeros = [1,2,3,4,5,6,9.5]
valores_cuadrado = [numero**2 for numero in numeros]
print(valores_cuadrado)

#Practica COmprension de Listas 2
numeros = [1,2,3,4,5,6,9.5]
valores_pares = [numero for numero in numeros if numero % 2 == 0]
print(valores_pares)

#Practica COmprension de Listas 3

temperatura_farenheit = [32,212,275]
temperatura_celsius = [(temperatura - 32) * (5/9) for temperatura in temperatura_farenheit]

print(temperatura_celsius)  