
"""
Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Curso: Programación
Universidad Nacional Abierta y a Distancia
Fase 4
"""

from decimal import Decimal, InvalidOperation

from clientes import Cliente

from servicios import (
    ReservaEspacio,
    AlquilerEquipo,
    Consultoria
)

from reservas import Reserva

from excepciones import (
    ErrorSistema,
    ErrorReserva,
    EstadoReservaInvalido,
    ReservaNoEncontrada
)

from logs import (
    registrar_evento,
    registrar_error,
    registrar_advertencia
)


# ==========================================================
# DATOS DEL SISTEMA INTERACTIVO
# ==========================================================

clientes = []
reservas = []

servicios = [
    ReservaEspacio(
        "Sala de reuniones",
        "Espacio para reuniones empresariales.",
        150000,
        20
    ),
    AlquilerEquipo(
        "Computador portátil",
        "Alquiler de equipo tecnológico.",
        80000,
        "Computador"
    ),
    Consultoria(
        "Asesoría tecnológica",
        "Orientación para proyectos tecnológicos.",
        200000,
        "Tecnología y software"
    )
]


# ==========================================================
# FUNCIONES GENERALES
# ==========================================================

def mostrar_titulo(mensaje):
    """Muestra los títulos de las secciones del sistema."""
    print("\n" + "=" * 60)
    print(mensaje)
    print("=" * 60)


def leer_porcentaje(mensaje):
    """Solicita un porcentaje numérico válido."""

    valor = input(mensaje).strip()

    try:
        porcentaje = Decimal(valor)
    except (InvalidOperation, ValueError):
        raise ValueError("Debe ingresar un valor numérico válido.")

    if not porcentaje.is_finite():
        raise ValueError("El porcentaje debe ser un número finito.")

    if not Decimal("0") <= porcentaje <= Decimal("100"):
        raise ValueError("El porcentaje debe estar entre 0 y 100.")

    return porcentaje


# ==========================================================
# GESTIÓN DE CLIENTES
# ==========================================================

def registrar_cliente():
    """Permite registrar un nuevo cliente."""

    mostrar_titulo("REGISTRO DE CLIENTE")

    try:
        identificador = f"CLI{len(clientes) + 1:03d}"

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        correo = input("Correo electrónico: ")
        telefono = input("Teléfono: ")

        cliente = Cliente(
            identificador,
            nombre,
            apellido,
            correo,
            telefono
        )

    except (ValueError, TypeError, ErrorSistema) as error:
        print(f"\nNo fue posible registrar el cliente: {error}")
        registrar_error(f"Error registrando cliente: {error}")

    else:
        clientes.append(cliente)

        print("\nCliente registrado correctamente.")
        print(cliente)

        registrar_evento(
            f"Cliente {identificador} registrado correctamente."
        )

    finally:
        print("\nFinalizó el proceso de registro.")


def mostrar_clientes():
    """Muestra los clientes registrados."""

    mostrar_titulo("CLIENTES REGISTRADOS")

    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print(cliente)
        print("-" * 50)


# ==========================================================
# CONSULTA DE SERVICIOS
# ==========================================================

def mostrar_servicios():
    """Muestra el catálogo de servicios disponibles."""

    mostrar_titulo("SERVICIOS DISPONIBLES")

    for indice, servicio in enumerate(servicios, start=1):
        print(f"\n{indice}. {servicio.nombre}")
        print(servicio.obtener_descripcion())
        print(f"Precio base: ${servicio.precio_base}")
        print("-" * 50)


# ==========================================================
# GESTIÓN DE RESERVAS
# ==========================================================

def crear_reserva():
    """Permite crear una reserva para un cliente."""

    mostrar_titulo("CREACIÓN DE RESERVA")

    try:
        if not clientes:
            raise ValueError(
                "Primero debe registrar un cliente."
            )

        print("\nCLIENTES REGISTRADOS:")

        for indice, cliente in enumerate(clientes, start=1):
            print(f"{indice}. {cliente.nombre} {cliente.apellido}")

        opcion_cliente = int(
            input("\nSeleccione el número del cliente: ")
        )

        if not 1 <= opcion_cliente <= len(clientes):
            raise ValueError("El cliente seleccionado no existe.")

        cliente = clientes[opcion_cliente - 1]

        mostrar_servicios()

        opcion_servicio = int(
            input("\nSeleccione el número del servicio: ")
        )

        if not 1 <= opcion_servicio <= len(servicios):
            raise ValueError("El servicio seleccionado no existe.")

        servicio = servicios[opcion_servicio - 1]

        identificador = f"RES{len(reservas) + 1:03d}"

        duracion = input(
            "\nIngrese la duración en horas o días, según el servicio: "
        )

        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion
        )

    except (ValueError, TypeError, ErrorSistema) as error:
        print(f"\nNo fue posible crear la reserva: {error}")
        registrar_error(f"Error creando reserva: {error}")

    else:
        reservas.append(reserva)

        print("\nReserva creada correctamente.")
        print(reserva)

        registrar_evento(
            f"Reserva {identificador} creada correctamente."
        )


def mostrar_reservas():
    """Muestra todas las reservas registradas."""

    mostrar_titulo("RESERVAS REGISTRADAS")

    if not reservas:
        print("No hay reservas registradas.")
        return

    for reserva in reservas:
        print(reserva)
        print("-" * 50)


def buscar_reserva():
    """Busca una reserva mediante su identificador."""

    identificador = input(
        "Ingrese el código de la reserva: "
    ).strip().upper()

    for reserva in reservas:
        if reserva.identificador == identificador:
            return reserva

    raise ReservaNoEncontrada(
        f"No se encontró la reserva {identificador}."
    )


def gestionar_reserva(accion):
    """Permite confirmar, cancelar o procesar una reserva."""

    mostrar_titulo(f"GESTIÓN DE RESERVA: {accion.upper()}")

    try:
        reserva = buscar_reserva()

        if accion == "confirmar":
            reserva.confirmar()
            print("\nReserva confirmada correctamente.")

        elif accion == "cancelar":
            reserva.cancelar()
            print("\nReserva cancelada correctamente.")

        elif accion == "procesar":

            impuesto = leer_porcentaje(
                "Ingrese el porcentaje de impuesto (0-100): "
            )

            descuento = leer_porcentaje(
                "Ingrese el porcentaje de descuento (0-100): "
            )

            costo = reserva.procesar(
                impuesto=impuesto,
                descuento=descuento
            )

            print("\nReserva procesada correctamente.")
            print(f"Costo final: ${costo}")

        else:
            raise ValueError("La acción solicitada no es válida.")

        print(reserva)

        registrar_evento(
            f"Reserva {reserva.identificador}: acción {accion}."
        )

    except (ErrorSistema, ValueError, TypeError) as error:
        print(f"\nNo se pudo realizar la operación: {error}")
        registrar_error(
            f"Error al gestionar reserva ({accion}): {error}"
        )


# ==========================================================
# MENÚ INTERACTIVO
# ==========================================================

def menu_interactivo():
    """Controla el menú principal de gestión."""

    registrar_evento("Menú interactivo iniciado.")

    while True:

        mostrar_titulo("MENÚ PRINCIPAL")

        print("1. Registrar cliente")
        print("2. Consultar clientes")
        print("3. Consultar servicios")
        print("4. Crear reserva")
        print("5. Mostrar reservas")
        print("6. Confirmar reserva")
        print("7. Cancelar reserva")
        print("8. Procesar reserva")
        print("0. Volver al menú inicial")

        opcion = input("\nSeleccione una opción: ").strip()

        try:

            if opcion == "1":
                registrar_cliente()

            elif opcion == "2":
                mostrar_clientes()

            elif opcion == "3":
                mostrar_servicios()

            elif opcion == "4":
                crear_reserva()

            elif opcion == "5":
                mostrar_reservas()

            elif opcion == "6":
                gestionar_reserva("confirmar")

            elif opcion == "7":
                gestionar_reserva("cancelar")

            elif opcion == "8":
                gestionar_reserva("procesar")

            elif opcion == "0":
                registrar_evento(
                    "Usuario regresó al menú inicial."
                )
                print("\nRegresando al menú inicial...")
                break

            else:
                registrar_advertencia(
                    f"Opción no válida en menú interactivo: {opcion}"
                )
                print("\nOpción no válida. Intente nuevamente.")

        except (ValueError, TypeError) as error:
            registrar_error(
                f"Error en el menú interactivo: {error}"
            )
            print(f"Se presentó un error: {error}")


# ==========================================================
# DEMOSTRACIÓN ACADÉMICA: 14 OPERACIONES
# ==========================================================

def demostracion_academica():
    """Ejecuta las 14 operaciones de demostración del proyecto."""

    print("\nIniciando demostración académica...")

    clientes_demo = []
    servicios_demo = []
    reservas_demo = []

    # OPERACIÓN 1: Registro correcto con try, except, else y finally.

    mostrar_titulo("OPERACIÓN 1: REGISTRO DE CLIENTE")

    try:
        cliente1 = Cliente(
            "CLI001",
            "Harvey",
            "Poveda",
            "harvey@example.com",
            "3001234567"
        )

        clientes_demo.append(cliente1)

    except (TypeError, ValueError) as error:
        registrar_error(f"Error registrando cliente: {error}")
        print(f"Error: {error}")

    else:
        registrar_evento(
            f"Cliente {cliente1.identificador} registrado."
        )
        print("Cliente registrado correctamente.")
        print(cliente1)

    finally:
        print("Finalizó la operación de registro.")

    # OPERACIÓN 2: Registro de segundo cliente.

    mostrar_titulo("OPERACIÓN 2: REGISTRO DE SEGUNDO CLIENTE")

    try:
        cliente2 = Cliente(
            "CLI002",
            "Laura",
            "Gomez",
            "laura@example.com",
            "3109876543"
        )

        clientes_demo.append(cliente2)

        registrar_evento(
            f"Cliente {cliente2.identificador} registrado."
        )

        print("Segundo cliente registrado.")
        print(cliente2)

    except (TypeError, ValueError) as error:
        registrar_error(f"Error registrando segundo cliente: {error}")
        print(f"Error: {error}")

    # OPERACIÓN 3: Registro de cliente inválido.

    mostrar_titulo("OPERACIÓN 3: VALIDACIÓN DE CLIENTE INVÁLIDO")

    try:
        cliente_invalido = Cliente(
            "CLI003",
            "Juan123",
            "Perez",
            "juan@example.com",
            "3001234567"
        )

        clientes_demo.append(cliente_invalido)

    except (TypeError, ValueError) as error:
        registrar_error(f"Registro rechazado: {error}")
        print(f"El cliente no pudo registrarse: {error}")

    # OPERACIÓN 4: Crear servicio de espacios.

    mostrar_titulo("OPERACIÓN 4: CREACIÓN DE RESERVA DE ESPACIO")

    espacio = ReservaEspacio(
        "Sala principal",
        "Sala para reuniones y eventos.",
        100000,
        30
    )

    servicios_demo.append(espacio)

    print("Servicio creado correctamente.")
    print(espacio.obtener_descripcion())

    # OPERACIÓN 5: Crear servicio de equipos.

    mostrar_titulo("OPERACIÓN 5: CREACIÓN DE ALQUILER DE EQUIPO")

    equipo = AlquilerEquipo(
        "Proyector",
        "Proyector multimedia HD.",
        50000,
        "Audiovisual"
    )

    servicios_demo.append(equipo)

    print("Servicio creado correctamente.")
    print(equipo.obtener_descripcion())

    # OPERACIÓN 6: Crear servicio de consultoría.

    mostrar_titulo("OPERACIÓN 6: CREACIÓN DE CONSULTORÍA")

    consultoria = Consultoria(
        "Asesoría tecnológica",
        "Orientación en soluciones informáticas.",
        80000,
        "Tecnología"
    )

    servicios_demo.append(consultoria)

    print("Servicio creado correctamente.")
    print(consultoria.obtener_descripcion())

    # OPERACIÓN 7: Crear reserva.

    mostrar_titulo("OPERACIÓN 7: CREACIÓN DE RESERVA")

    reserva1 = Reserva(
        "RES001",
        cliente1,
        espacio,
        2
    )

    reservas_demo.append(reserva1)

    print("Reserva creada correctamente.")
    print(reserva1)

    # OPERACIÓN 8: Confirmar reserva.

    mostrar_titulo("OPERACIÓN 8: CONFIRMACIÓN DE RESERVA")

    reserva1.confirmar()

    print("Reserva confirmada.")
    print(f"Estado actual: {reserva1.estado}")

    # OPERACIÓN 9: Calcular costo.

    mostrar_titulo("OPERACIÓN 9: CÁLCULO DEL COSTO")

    costo = reserva1.calcular_costo(
        impuesto=19,
        descuento=10
    )

    print(f"Servicio: {reserva1.servicio.nombre}")
    print(f"Duración: {reserva1.duracion} horas")
    print("Impuesto: 19 %")
    print("Descuento: 10 %")
    print(f"Costo total: ${costo}")

    # OPERACIÓN 10: Procesar reserva.

    mostrar_titulo("OPERACIÓN 10: PROCESAMIENTO DE RESERVA")

    costo_final = reserva1.procesar(
        impuesto=19,
        descuento=10
    )

    print("Reserva procesada correctamente.")
    print(f"Costo final: ${costo_final}")
    print(f"Estado actual: {reserva1.estado}")

    # OPERACIÓN 11: Crear y cancelar otra reserva.

    mostrar_titulo("OPERACIÓN 11: CANCELACIÓN DE RESERVA")

    reserva2 = Reserva(
        "RES002",
        cliente2,
        equipo,
        3
    )

    reservas_demo.append(reserva2)

    print("Segunda reserva creada.")
    print(reserva2)

    reserva2.cancelar()

    print("Reserva cancelada correctamente.")
    print(f"Estado actual: {reserva2.estado}")

    # OPERACIÓN 12: Intentar procesar una reserva pendiente.

    mostrar_titulo("OPERACIÓN 12: CONTROL DE ESTADOS")

    reserva3 = Reserva(
        "RES003",
        cliente1,
        consultoria,
        2
    )

    reservas_demo.append(reserva3)

    try:
        reserva3.procesar()

    except EstadoReservaInvalido as error:
        registrar_error(
            f"Operación no permitida en "
            f"{reserva3.identificador}: {error}"
        )
        print(f"Operación rechazada correctamente: {error}")

    # OPERACIÓN 13: Intentar crear una reserva inválida.

    mostrar_titulo("OPERACIÓN 13: VALIDACIÓN DE RESERVA")

    try:
        Reserva(
            "RES004",
            cliente1,
            espacio,
            -5
        )

    except ValueError as error:
        registrar_error(f"Reserva inválida: {error}")
        print(f"No fue posible crear la reserva: {error}")

    # OPERACIÓN 14: Encadenamiento de excepciones.

    mostrar_titulo("OPERACIÓN 14: ENCADENAMIENTO DE EXCEPCIONES")

    try:
        reserva3.calcular_costo(impuesto=150)

    except ErrorReserva as error:
        registrar_error(
            f"Error encadenado en reserva "
            f"{reserva3.identificador}: {error}"
        )

        print(f"Excepción principal: {error}")

        if error.__cause__ is not None:
            print(
                "Excepción original:",
                type(error.__cause__).__name__
            )
            print("Detalle original:", error.__cause__)

    # RESUMEN DE LA DEMOSTRACIÓN.

    mostrar_titulo("RESUMEN GENERAL DE LA DEMOSTRACIÓN")

    print(f"Clientes registrados: {len(clientes_demo)}")
    print(f"Servicios creados: {len(servicios_demo)}")
    print(f"Reservas creadas: {len(reservas_demo)}")

    print("\nESTADO DE LAS RESERVAS:")

    for reserva in reservas_demo:
        print(reserva)

    registrar_evento(
        "Finalización de las 14 operaciones de demostración."
    )

    print("\nDemostración académica finalizada.")


# ==========================================================
# INICIO DEL SISTEMA
# ==========================================================

def iniciar_sistema():
    """Presenta las modalidades de ejecución del sistema."""

    registrar_evento("Sistema Software FJ iniciado.")

    while True:

        mostrar_titulo(
            "SISTEMA INTEGRAL DE GESTIÓN SOFTWARE FJ"
        )

        print("Gestión de Clientes, Servicios y Reservas\n")
        print("1. Ejecutar demostración académica (14 operaciones)")
        print("2. Ingresar al menú interactivo")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            try:
                demostracion_academica()

            except (ErrorSistema, ValueError, TypeError) as error:
                registrar_error(
                    f"Error en la demostración académica: {error}"
                )
                print(f"Error durante la demostración: {error}")

        elif opcion == "2":
            menu_interactivo()

        elif opcion == "0":
            registrar_evento("Sistema Software FJ finalizado.")
            print("\nGracias por utilizar Software FJ.")
            break

        else:
            registrar_advertencia(
                f"Opción no válida en menú inicial: {opcion}"
            )
            print("\nOpción no válida. Intente nuevamente.")


# Punto de entrada de la aplicación.

if __name__ == "__main__":
    iniciar_sistema()
