import datos


def limpiar_pantalla(): #
    import os
    os.system("cls" if os.name == "nt" else "clear")


def identificar_empleado():
    print("\n IDENTIFICACIÓN ")
    nombre = input("Ingresá tu nombre: ").strip()
    if not nombre:
        print("Error: el nombre no puede estar vacío.")
        return None, None

    dni = input("Ingresá tu DNI: ").strip()
    if not dni.isdigit():
        print("Error: el DNI debe contener solo números.")
        return None, None

    empleado = datos.buscar_empleado(dni)
    if not empleado:
        print("Error: no se encontró ningún empleado con ese DNI.")
        return None, None

    print(f"\nBienvenido/a, {empleado['nombre']}.")
    return dni, empleado


def opcion_solicitar(dni, empleado):
    print("\n SOLICITAR VACACIONES ")
    dias_disponibles = int(empleado["dias_disponibles"])
    print(f"Días disponibles: {dias_disponibles}")

    dias_input = input("¿Cuántos días querés solicitar? ").strip()

    # camino infeliz: entrada no numérica
    if not dias_input.isdigit():
        print("Error: ingresá un número válido.")
        return

    dias = int(dias_input)

    # camino infeliz: cero o negativo
    if dias <= 0:
        print("Error: la cantidad de días debe ser mayor a cero.")
        return

    # compuerta 2: ¿tiene días suficientes?
    if dias > dias_disponibles:
        print(f"Error: no tenés suficientes días. Disponibles: {dias_disponibles}.")
        return

    datos.registrar_solicitud(dni, empleado["nombre"], dias)
    print(f"\nSolicitud registrada correctamente.")
    print(f"Días restantes: {dias_disponibles - dias}")


def opcion_consultar(dni):
    print("\n CONSULTAR DÍAS DISPONIBLES ")
    dias = datos.consultar_dias(dni)
    if dias is not None:
        print(f"Tenés {dias} día/s disponibles.")
    else:
        print("Error al consultar los días.")


def opcion_ver_solicitudes(dni):
    print("\n MIS SOLICITUDES ANTERIORES ")
    solicitudes = datos.ver_solicitudes(dni)
    if not solicitudes:
        print("No tenés solicitudes registradas.")
        return
    for i, s in enumerate(solicitudes):
        print(f"{i + 1}. {s['dias_solicitados']} día/s solicitados")


def opcion_cancelar(dni):
    print("\n CANCELAR UNA SOLICITUD ")
    solicitudes = datos.ver_solicitudes(dni)
    if not solicitudes:
        print("No tenés solicitudes para cancelar.")
        return

    for i, s in enumerate(solicitudes):
        print(f"{i + 1}. {s['dias_solicitados']} día/s solicitados")

    seleccion = input("Ingresá el número de la solicitud a cancelar: ").strip()

    # camino infeliz: entrada no numérica
    if not seleccion.isdigit():
        print("Error: ingresá un número válido.")
        return

    indice = int(seleccion) - 1
    exito = datos.cancelar_solicitud(dni, indice)

    if exito:
        print("Solicitud cancelada. Los días fueron devueltos a tu saldo.")
    else:
        print("Error: número de solicitud inválido.")


def menu_principal():
    print("""
        1. Solicitar vacaciones
        2. Consultar días disponibles
        3. Ver mis solicitudes
        4. Cancelar solicitud
        5. Salir
        """)
    return input("Elegí una opción (1-5): ").strip()


def main():
    limpiar_pantalla()
    print("Bienvenido al sistema de gestión de vacaciones.")

    # identificación una sola vez al inicio
    dni, empleado = None, None
    while not dni:
        dni, empleado = identificar_empleado()
        if not dni:
            reintentar = input("¿Querés intentarlo de nuevo? (s/n): ").strip().lower()
            if reintentar != "s":
                print("Hasta luego.")
                return

    # loop del menú
    while True:
        opcion = menu_principal()

        if opcion == "1":
            # recargamos el empleado para tener los días actualizados
            empleado = datos.buscar_empleado(dni)
            opcion_solicitar(dni, empleado)
        elif opcion == "2":
            opcion_consultar(dni)
        elif opcion == "3":
            opcion_ver_solicitudes(dni)
        elif opcion == "4":
            opcion_cancelar(dni)
        elif opcion == "5":
            print("\nHasta luego.")
            break
        else:
            print("Opción inválida. Ingresá un número del 1 al 5.")

        input("\nPresioná Enter para continuar.")
        limpiar_pantalla()


main()
