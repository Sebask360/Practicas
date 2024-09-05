#Practica Metodo Index()1
print("Practicas de metodo index()")
palabra = "ordenador"

quinto = palabra[4]
print(quinto)

#Practica Metodo Index()2

frase = "En teoria, la teoria y la practica son los mismos. En la practica, no lo son"

indice_palabra = frase.index("practica")

print(f"El indice de la primera aparicion de 'practica' es: {indice_palabra}")

#Practica Metodo Index()3

indice_palabra = frase.rindex("practica")

print(f"El indice de la primera aparicion de 'practica' es: {indice_palabra}\n")

#Practica Sub-strings 1
print("Practicas substrings")

frase = "Controlar la complejidad es la esencia de la prigramacion"
print(frase[0:9])

#Practica Sub-strings 2

frase = "Nunca confies en un ordenador que no puedas lanzar por la ventana"
print(frase[3::3])

#Practica Sub-strings 3

frase = "Es genial trabajar con ordenadores. No discutenn, lo recuerdan todo y no se beben tu cerveza"
print(f"{frase [::-1]}\n")

#Practica Metodos de String 
print("Practica Metodods de String")

#Practica Metodos de String 1
frase = "Si la implementacion es dificil de explicar, puede que sea una mala idea"

frase_mayus = frase.upper

print(frase_mayus)

#Practica Metodos de String 2

#Practica Metodos de String 3


frase_nueva = frase.replace("dificil", "facil").replace("mala", "buena")

print(frase_nueva)

