# Practica operadores de comparacion 1
num1 = 36
num2 = 17

mi_bool= (num1 >= num2)
print(mi_bool)

# Practica operadores de comparacion 2
num1 = (25 **0.5)
num2 = 5

mi_bool = (num1 == num2)
print(mi_bool)

# Practica operadores de comparacion 3

num1 = (64 * 3)
num2 = (24 * 8)

mi_bool = num1 != num2
print(mi_bool)

#Practica Operadores Logicos 1
num1 = 36
num2 = (72/2)
num3 = 48

mi_bool = num1 > num2  and num1 < num3
print(mi_bool)

#Practica Operadores Logicos 2
num1 = 36
num2 = (72/2)
num3 = 48

mi_bool = num1 > num3 or num1 < num3
print(mi_bool)

#Practica Control de Flujo 1
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

f"{num1} es mayor que {num2}"
"num2 es mayor que num1"
"num1 y num2 son iguales"

if num1 > num2:
    print(f"{num1} es mayor que {num2}.")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}.")
elif num1 == num2:
    print(f"{num1} y {num2} son iguales.")

# Practica Control de Flujo 2
edad = int(input("Ingresa tu edad: "))
tiene_licencia = input("Tienes licencia? (s/n)") 
if tiene_licencia != "s":
     tiene_licencia = False
else:
     tiene_licencia = True

if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad < 18 and tiene_licencia != False:
     print("No puedes conducir aun. Debes tener 18 años y contar con una licencia")
else:
     print("No puedes conducir. Necesitas contar con una licencia")

#Practica Control de Flujo 3
sabe_python = input("¿Sabes programar en Python? ")
sabe_ingles = input("¿Sabes hablar en Ingles? ")

if sabe_python != "s":
     sabe_python = False
else:
     sabe_python = True

if sabe_ingles != "s":
     sabe_ingles = False
else:
     sabe_ingles = True

if sabe_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif sabe_ingles == False and sabe_python == False:
    print("Para postuarte, necesitas saber programar en Python y tener conocimientos de ingles")
elif sabe_python == True and sabe_ingles == False:
    print("Para postularte, necesitas tener conocimientos de ingles")
elif sabe_python == False and sabe_ingles == True:
    print("Para postularte, necesitas tener conocimientos de Python")