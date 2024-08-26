import random

palabras = ["casa", "coche", "arbol", "pelicula", "musica"]

palabra_secreta = random.choice(palabras)

vidas = 6
palabra_mostrada = ["_"] * len(palabra_secreta)

def pedir_letra():
    letra = input("Elige una letra: ")
    return letra

def es_letra_valida(letra):
    return len(letra) == 1 and letra.isalpha()

def esta_en_palabra(letra):
    return letra in palabra_secreta

def actualizar_palabra(letra):
    global palabra_mostrada
    for i, letra_secreta in enumerate(palabra_secreta):
        if letra_secreta == letra:
            palabra_mostrada[i] = letra

def ha_ganado():
    return "_" not in palabra_mostrada

def jugar():
    global vidas
    while vidas > 0 and not ha_ganado():
        print(" ".join(palabra_mostrada))
        letra = pedir_letra()
        if es_letra_valida(letra):
            if esta_en_palabra(letra):
                actualizar_palabra(letra)
            else:
                vidas -= 1
                print(f"Te quedan {vidas} vidas")
        else:
            print("Ingrese una letra válida")
    if ha_ganado():
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

jugar()
