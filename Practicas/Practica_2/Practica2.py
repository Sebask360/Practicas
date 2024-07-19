# Practica de Formatear Cadenas

# Practica de Formatear Cadenas 1

nombre_asociado =  input("Ingresa su nombre asociado: ")
numero_asociado = input("Ingresa tu numero asociado: ")

print(f"\nEstimado/a {nombre_asociado}, su numero de asociado es: {numero_asociado} \n")

#Practica de Formatear Cadenas 2

import random 

puntos_nuevos = random.randint(1, 100)
puntos_totales = 3450
puntos_actuales = puntos_nuevos + puntos_totales

print("Tenias {}, y has ganado {} nuevos puntos. En total, acumulas {} puntos".format(puntos_totales, puntos_nuevos, puntos_actuales))
print(f"Tenias {puntos_totales}, y has ganado {puntos_nuevos} nuevos puntos. En total, acumulas {puntos_actuales} puntos")

# Practica de Formatear Cadenas 3

puntos_nuevos = random.randint(50, 150)
puntos_totales = puntos_actuales 
puntos_actuales = puntos_nuevos + puntos_totales

print("Tenias {}, y has ganado {} nuevos puntos. En total, acumulas {} puntos".format(puntos_totales, puntos_nuevos, puntos_actuales))
print(f"Tenias {puntos_totales}, y has ganado {puntos_nuevos} nuevos puntos. En total, acumulas {puntos_actuales} puntos\n")

puntos_totales = puntos_actuales

print(f"Hola {nombre_asociado} a continuacion te dare tus datos:\nNumero asociado: {numero_asociado}.\nPuntos totales en tu cuenta: {puntos_totales}.\n")

numerador = 874
denominador = 27

cociente = numerador//denominador
print(f"{numerador} dividido entre {denominador} es igual a {cociente}")

# Practica Operadores Matematicos 2

num1 = 456
num2 = 33

print(f"El modulo entre {num1}, y {num2} es: {num1%num2}")

# Practica Operadores Matematicos 3

num1 = 783
print(f"La raiz cuadrada de {num1} es: {num1**0.5}\n")

# Practica Redondeo 1

num1 = 10 
num2 = 3
resultado = 10/3 
resultado = round(resultado, 2)

print(f"El resultado de la division entre: {num1} y {num2} es:\n{num1/num2}\nRedondeado: {resultado}\n")

# Practica Redondeo 2

print(f"El entero más próximo de 10.676767 es: {round(10.676767)}\n")

# Practica de Redondeo 3

print(f"La raiz cuadrada de 5 es: {round(5**0.5, 4)} \n")