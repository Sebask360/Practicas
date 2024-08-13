#Practica Enumerador 1
lista_nombres = ["Marcos","Laura","Monica","Celina","Marta","Dario","Emiliano","Melina"]
for indice, nombre in enumerate(lista_nombres):
    print(f"{nombre} de encuentra en el indice {indice}")
#Practica Enumerador 2
palabra = "Python"
lista_indices = list(enumerate(palabra))
print(lista_indices)

#Practica Enumerador 3
lista_nombres = ["Marcos","Laura","Monica","Celina","Marta","Dario","Emiliano","Melina"]
for index, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(f"Indice: {index}, Nombre: {nombre}")

#Practica Zip 1
capitales = ["Berlin", "Tokio","Paris", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japon", "Francia", "Finlandia", "Canada","Australia"]
for capitales, paises in zip(capitales, paises):
    print(f'La capital de {paises} es {capitales}')

#Practica Zip 2
marcas = ["Pepsi", "Intel", "Samsung", "Acer", "Yamaha", "Sony"]
productos = ["Gaseosas", "Procesadores", "Telefonos", "Computadores", "Motocicletas", "Consolas"]
for marcas, productos in zip(marcas,productos):
    print(f"La marca {marcas} hace {productos.lower()}.")

#Practica Zip 3
ingles = ["one", "two","three","four","five"]
portugues = ["um","dois","três","quatro","cinco"]
español = ["uno", "dos", "tres","cuatro","cinco"]

numeros = list(zip(español,portugues,ingles))
print(numeros)

for i, (ingles, español, portugues) in enumerate(numeros, start=1):
    print(f"{i}. {español} / {ingles} / {portugues}")

#Practica Min y Max 1
lista_numeros = [4454247/2,2134747*33,44556475,121676,6654867,353254,123134,55**12,611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)

#Practica Min y Max 2
lista_numeros = [44542247,21310,2134747,44556475,121676,6654067,353254,123134,552512,611665]
valor_max = max(lista_numeros)
valor_min = min(lista_numeros)

print(valor_max)
print(valor_min)

rango = valor_max - valor_min
print(rango)

#Practica Min y Max 3
diccionario_edades = {"Carlos":55, "María": 42, "Mabel":78, "José": 44, "Lucas":24, "Rocio":35, "Sebastián": 19, "Catalina": 2, "Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())

print(f"La edad mínima es: {edad_minima}")
print(f"El nombre último en orden alfabético es: {ultimo_nombre}")
