# Asistente de Finanzas Personales Básico

# -------------------------------
# VARIABLES GLOBALES (ASSIGNMENT)
# -------------------------------
totalIngresos = 0.0
totalGastos = 0.0

# -------------------------------
# FUNCIONES (CALL)
# -------------------------------

def registrarIngreso():
    global totalIngresos
    try:
        montoIngreso = float(input("Ingrese el monto del ingreso: "))
        # SELECTION: ¿montoIngreso > 0?
        if montoIngreso > 0:
            # ASSIGNMENT: totalIngresos ← totalIngresos + montoIngreso
            totalIngresos = totalIngresos + montoIngreso
            print("Ingreso registrado.")
        else:
            print("Error: monto inválido (debe ser mayor que 0).")
    except ValueError:
        print("Error: debe ingresar un número válido.")


def registrarGasto():
    global totalGastos
    try:
        montoGasto = float(input("Ingrese el monto del gasto: "))
        # SELECTION: ¿montoGasto > 0?
        if montoGasto > 0:
            # ASSIGNMENT: totalGastos ← totalGastos + montoGasto
            totalGastos = totalGastos + montoGasto
            print("Gasto registrado.")
        else:
            print("Error: monto inválido (debe ser mayor que 0).")
    except ValueError:
        print("Error: debe ingresar un número válido.")


def calcularBalance():
    # ASSIGNMENT: balance ← totalIngresos - totalGastos
    balance = totalIngresos - totalGastos
    # SELECTION: ¿balance < 0?
    if balance < 0:
        print("Alerta: balance negativo.")
    print("Balance actual:", balance)


def mostrarResumen():
    print("\n--- RESUMEN FINANCIERO ---")
    print("Ingresos totales:", totalIngresos)
    print("Gastos totales:", totalGastos)
    print("Balance:", totalIngresos - totalGastos)


# -------------------------------
# MENÚ PRINCIPAL (LOOP: opción != 5)
# -------------------------------

def mostrarMenu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Ver balance")
    print("4. Ver resumen")
    print("5. Salir")


def main():
    opcion = 0
    # LOOP: mientras opción != 5
    while opcion != 5:
        mostrarMenu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: debe ingresar un número de opción.")
            continue

        # SELECTION: ¿opción?
        if opcion == 1:
            registrarIngreso()      # CALL
        elif opcion == 2:
            registrarGasto()        # CALL
        elif opcion == 3:
            calcularBalance()       # CALL
        elif opcion == 4:
            mostrarResumen()        # CALL
        elif opcion == 5:
            print("Fin del sistema.")
        else:
            print("Opción inválida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
