nombre = input("Por favor, ingresa tu nombre completo: ")
ventas = input("Ingresa cuanto has vendido en total: ")

ventas = float(ventas)

comision = (ventas * 13) / 100

comision_decim = round(comision, 2)

print(f"Bienvenido {nombre}, tu comisión por este mes ha sido de ${comision_decim}.") 