def imprimir_recuadro(texto):
  lines = texto.split('\n')
  max_length = max(len(lines) for lines in lines)
  border = '+' + '-' * (max_length +2) + '+'
  
  print(border)
  for lines in lines:
    print(f'| {lines.ljust(max_length)} |')
  print(border)
  
nombre = input("Ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
nombrecompleto = ((nombre)+ " " +str(apellido))

num_uno = input("Ingrese un numero: ")
num_int = float(num_uno)
doble_numero = num_int * 2

texto = (
  f"\nBienvenido {nombrecompleto}, Tienes {edad} años\n\n"\
  f"Ingresaste {num_int}, y el doble de {num_int} es {doble_numero}\n"
)

imprimir_recuadro(texto)