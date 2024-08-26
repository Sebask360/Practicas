import random
#Practica Crear Funciones 1
def saludar():
    print("¡Hola Mundo!")

saludar()

#Practica Crear Funciones 2
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen", "Alejandra"]
nombre_persona = random.choice(nombres)
def bienvenida():
    print(f"¡Bienvenido/a {nombre_persona}!")
bienvenida()
#Practica Crear Funciones 3
un_numero = random.randint(1,10)
def cuadrado(un_numero):
    print(f"El cuadrado de {un_numero} es:{un_numero ** 2}")

cuadrado(un_numero)

#Practica Return 1
num1 = random.randint(1,10)
num2 = random.randint(1,10)

def potencia():
    return(num1**num2)

resultado = potencia()

print(f"La base es: {num1}")
print(f"El exponente es: {num2}")
print(f"La potencia es: {resultado}")

#Practica Return 2

dolares = input("Ingrese el valor del monto en dolares:")
def usd_a_eur(dolares):
    return int(dolares) * 0.90

resultado = usd_a_eur(dolares)
print((resultado))

#Practica Return 3
palabra = "Python"
def invertir_palabra(palabra):
    return (palabra[::-1].upper())

resultado = invertir_palabra(palabra)
print(resultado)