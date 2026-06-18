# Bot de Gestión de Vacaciones
**Trabajo Práctico Integrador — Organización Empresarial | UTN TUP**

Simulador de chatbot en consola que automatiza el proceso de solicitud de vacaciones de una empresa ficticia. El sistema permite al empleado identificarse, solicitar días, consultar su saldo y gestionar sus solicitudes, todo con persistencia en archivos CSV.

---

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `bot.py` | Programa principal. Contiene el menú y la lógica de interacción con el usuario. |
| `datos.py` | Módulo de acceso a datos. Funciones para leer y escribir los archivos CSV. |
| `empleados.csv` | Base de datos de empleados con nombre, DNI y días disponibles. |
| `solicitudes.csv` | Se genera automáticamente al registrar la primera solicitud. |

---

## Requisitos

- Python 3.x
- No requiere librerías externas (solo módulos estándar: `csv`, `os`)

---

## Cómo ejecutarlo

1. Cloná el repositorio o descargá los archivos.
2. Asegurate de que `bot.py`, `datos.py` y `empleados.csv` estén en la misma carpeta.
3. Desde la terminal, ejecutá:

```bash
python bot.py
```

> En Linux/Mac puede ser necesario usar `python3 bot.py`

---

## Funcionalidades

| Opción | Descripción |
|---|---|
| 1. Solicitar vacaciones | Ingresa la cantidad de días a solicitar. Valida saldo disponible. |
| 2. Consultar días disponibles | Muestra el saldo actual de días del empleado. |
| 3. Ver solicitudes anteriores | Lista todas las solicitudes registradas. |
| 4. Cancelar una solicitud | Cancela una solicitud y devuelve los días al saldo. |
| 5. Salir | Cierra el programa. |

---

## Empleados de prueba

| DNI | Nombre | Días disponibles |
|---|---|---|
| 30456782 | Martín Rodríguez | 15 |
| 27891034 | Laura Fernández | 8 |
| 28743210 | Valeria Méndez | 0 ← para probar error de días insuficientes |

---

## Estructura del proceso (BPMN)

El flujo del bot responde al diagrama BPMN 2.0 diseñado para el trabajo:
1. El empleado se identifica con nombre y DNI.
2. El sistema verifica su existencia en la base de datos (**Compuerta 1**).
3. Se muestra el menú de opciones.
4. Según la opción elegida, el sistema ejecuta la lógica correspondiente.
5. En la opción 1, se valida si tiene días suficientes (**Compuerta 2**).
6. Todas las opciones vuelven al menú hasta que el usuario elige Salir.
