nombre = input("Inngresa tu nombre: ")
ventas = float(input("Ingresa el total de tus ventas: "))

comision = ventas * 13 / 100
comision_f = "{:.2f}".format(comision)

print(f"Hola {nombre}, tu total de ventas es ${ventas} y tu comision es de ${comision_f} ")