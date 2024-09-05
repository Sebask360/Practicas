# #Practica sobre interaccion entre Funciones 1
# import random
# def lanzar_dados():
#     dado1 = random.randint(1,6)
#     dado2 = random.randint(1,6)

#     return dado1, dado2

# def evaluar_jugada(dado1,dado2):
#     suma_dados = dado1 + dado2

#     if suma_dados <= 6:
#         return(f"La suma de tus dados es {suma_dados}. lametablemete")
#     elif 7 <= suma_dados  < 10:
#         return(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
#     else:
#         return(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

# dado1, dado2 = lanzar_dados()
# resultado = evaluar_jugada(dado1,dado2)
# print(resultado)

# #Practica sobre interaccion entre Funciones 2
# def  reducir_lista(lista_numeros):
#     lista_sin_duplicado = list(set(lista_numeros))
#     lista_sin_duplicado.remove(max(lista_sin_duplicado))

#     return lista_sin_duplicado

# def promedio(lista_reducida):
#     if len(lista_reducida) ==0:
#         return 0
#     return sum(lista_reducida) / len(lista_reducida)

# lista_numeros = [1,2,15,7,2]
# lista_reducida = reducir_lista(lista_numeros)
# resultado_promedio = promedio(lista_reducida)

# print(f"Lista despues de reducir: {lista_reducida}")
# print(f"El promedio de la lista despues de reducirla {resultado_promedio}")

# #Practicas sobre argumentos indefinidos (*args) 1

# def suma_cuadrados(*args):

#     return sum(numeros **2 for numeros in args)

# resultado = suma_cuadrados(1,2,3)
# print(f"La suma de los cuadrados de los numeros es: {resultado}")
    
# #Practicas sobre argumentos indefinidos (*args) 2
# def suma_absolutos(*args):
    
#     return sum(abs(numeros) for numeros in args)

# resultado = suma_absolutos(-1,2,-3,4,-5,-6)
# print(f"La suma de los valores absolutos es: {resultado}")

# #Practicas sobre argumentos indefinidos (*args) 3
def numeros_persona(nombre, *args):
    numeros_sumados = sum(args)
    return(f"{nombre}, la suma  de tus numeros es {numeros_sumados}")

resultado =  numeros_persona("Sebastian", 1,2,3,4) 
print(resultado)

#Practica sobre argumentos indefinifos (**kwargs) 1
def  cantidad_atributos(**kwargs):
    return len(kwargs)

resultado = cantidad_atributos(nombre="Sebastian", edad=20, ciudad="Pasto", ojos="cafes")

print(resultado)

#Practica sobre argumentos indefinifos (**kwargs) 2
def lista_atributos(**kwargs):
    return list(kwargs.values())

resultado = lista_atributos(Nombre="Sebastian", Edad=20, Ciudad="Pasto", Ojos="cafes")
print(f"Lista de atributos: {resultado}")

#Practica sobre argumentos indefinifos (**kwargs) 3
def describir_persona(nombre="Sebastian", **kwargs):
    print(f"1| Caracteristicas de {nombre}: ")
    contador = 2 
    for clave, valor in kwargs.items():
        print(f"{contador}| {clave}: {valor}")
        contador += 1

describir_persona("Sebastian", Edad=20, Ciudad="Pasto", Ojos="Cafes")