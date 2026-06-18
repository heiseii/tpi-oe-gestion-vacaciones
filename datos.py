import csv
import os

ARCHIVO_EMPLEADOS = "empleados.csv"
ARCHIVO_SOLICITUDES = "solicitudes.csv"


def buscar_empleado(dni):
    try:
        with open(ARCHIVO_EMPLEADOS, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["dni"] == dni:
                    return fila
    except FileNotFoundError:
        print("Error: no se encontró el archivo de empleados.")
    return None


def consultar_dias(dni):
    empleado = buscar_empleado(dni)
    if empleado:
        return int(empleado["dias_disponibles"])
    return None


def registrar_solicitud(dni, nombre, dias):
    archivo_existe = os.path.exists(ARCHIVO_SOLICITUDES)
    with open(ARCHIVO_SOLICITUDES, "a", newline="", encoding="utf-8") as archivo:
        campos = ["dni", "nombre", "dias_solicitados"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if not archivo_existe:
            escritor.writeheader()
        escritor.writerow({"dni": dni, "nombre": nombre, "dias_solicitados": dias})

    # actualizar días disponibles en empleados.csv
    filas = []
    with open(ARCHIVO_EMPLEADOS, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        campos_empleados = lector.fieldnames
        for fila in lector:
            if fila["dni"] == dni:
                fila["dias_disponibles"] = str(int(fila["dias_disponibles"]) - dias)
            filas.append(fila)

    with open(ARCHIVO_EMPLEADOS, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos_empleados)
        escritor.writeheader()
        escritor.writerows(filas)


def ver_solicitudes(dni):
    if not os.path.exists(ARCHIVO_SOLICITUDES):
        return []
    solicitudes = []
    with open(ARCHIVO_SOLICITUDES, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["dni"] == dni:
                solicitudes.append(fila)
    return solicitudes


def cancelar_solicitud(dni, indice):
    if not os.path.exists(ARCHIVO_SOLICITUDES):
        return False

    solicitudes_empleado = []
    todas = []
    with open(ARCHIVO_SOLICITUDES, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        campos = lector.fieldnames
        for fila in lector:
            todas.append(fila)
            if fila["dni"] == dni:
                solicitudes_empleado.append(fila)

    if indice < 0 or indice >= len(solicitudes_empleado):
        return False

    solicitud_a_cancelar = solicitudes_empleado[indice]
    dias_a_devolver = int(solicitud_a_cancelar["dias_solicitados"])

    todas.remove(solicitud_a_cancelar)

    with open(ARCHIVO_SOLICITUDES, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(todas)

    # devolver los días al empleado
    filas = []
    with open(ARCHIVO_EMPLEADOS, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        campos_empleados = lector.fieldnames
        for fila in lector:
            if fila["dni"] == dni:
                fila["dias_disponibles"] = str(int(fila["dias_disponibles"]) + dias_a_devolver)
            filas.append(fila)

    with open(ARCHIVO_EMPLEADOS, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos_empleados)
        escritor.writeheader()
        escritor.writerows(filas)

    return True
