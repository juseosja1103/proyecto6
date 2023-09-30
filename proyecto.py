class Gasto:
    def __init__(self, descripcion, monto):
        self.descripcion = descripcion
        self.monto = monto

class Presupuesto:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.gastos = []

    def registrar_gasto(self, descripcion, monto):
        if monto <= self.saldo:
            self.gastos.append(Gasto(descripcion, monto))
            print(f"Gasto de ${monto} registrado con éxito.")
        else:
            print("No tienes suficiente saldo para este gasto.")

    def calcular_presupuesto_actual(self):
        presupuesto_actual = self.saldo
        for gasto in self.gastos:
            presupuesto_actual -= gasto.monto
        return presupuesto_actual

def main():
    saldo_inicial = float(input("Ingresa tu saldo inicial: "))
    presupuesto = Presupuesto(saldo_inicial)

    while True:
        print("\nMenú:")
        print("1. Registrar un gasto")
        print("2. Calcular el presupuesto actual")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción del gasto: ")
            monto = int(input("Ingrese el monto del gasto: "))
            presupuesto.registrar_gasto(descripcion, monto)
        elif opcion == "2":
            presupuesto_actual = presupuesto.calcular_presupuesto_actual()
            print(f"Tu presupuesto actual es: ${presupuesto_actual}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
