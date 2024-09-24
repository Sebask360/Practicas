class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular 
        self.saldo = saldo

    def __str__(self):
        return f"Titular: {self.titular}\nSaldo: {self.saldo}"

class Banco:
    def __init__(self, nombre, listaCuentas=None):
        self.nombre = nombre
        self.listaCuentas = listaCuentas if listaCuentas is not None else []

    def agregarCuentas(self, cuenta):
        self.listaCuentas.append(cuenta)
        print(f"La cuenta de {cuenta.titular} ha sido agregada al banco {self.nombre}")

    def eliminarCuentas(self, titularCuenta):
        for cuenta in self.listaCuentas:
            if cuenta.titular == titularCuenta:
                self.listaCuentas.remove(cuenta)
                print(f"La cuenta de {titularCuenta} ha sido eliminada del banco {self.nombre}")
                return
        print(f"La cuenta {titularCuenta} no se encuentra en el banco {self.nombre}")

    def mostrarCuentas(self):
        if self.listaCuentas:
            print(f"Cuentas inscritas en el banco {self.nombre}:")
            for cuenta in self.listaCuentas:
                print(cuenta)
        else:
            print(f"No hay cuentas inscritas en el banco {self.nombre}")
    
    def buscarCuentas(self, titularCuenta):
        for cuenta in self.listaCuentas:
            if cuenta.titular == titularCuenta:
                print(f"Cuenta encontrada:\n{cuenta}")
                return
        print(f"No se encontró una cuenta de {titularCuenta}")
        
def mostrarMenu():
    print("\n===== Menú del Banco =====")
    print("1. Agregar cuenta")
    print("2. Eliminar cuenta")
    print("3. Mostrar cuentas")
    print("4. Buscar cuenta")
    print("5. Salir")
    print("=========================")

bancoS = Banco("Bancolombia")

def main():
    while True:
        mostrarMenu()
        opcion = int(input("Ingrese la opción: "))

        if opcion == 1:
            titular = input("Introduce el nombre del titular de la cuenta: ")
            saldo = float(input("Introduce el saldo inicial: "))
            nuevaCuenta = Cuenta(titular, saldo)
            bancoS.agregarCuentas(nuevaCuenta)

        elif opcion == 2:
            titular = input("Introduce el nombre del titular de la cuenta: ")
            bancoS.eliminarCuentas(titular)
            
        elif opcion == 3:
            bancoS.mostrarCuentas()
        
        elif opcion == 4:
            titular = input("Introduce el nombre del titular de la cuenta a buscar: ")
            bancoS.buscarCuentas(titular)
        
        elif opcion == 5:
            print("Gracias por usar nuestros servicios.")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecuta el programa
main()
