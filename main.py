
"""
Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Curso: Programación
Universidad Nacional Abierta y a Distancia
Fase 4
"""

from clientes import Cliente
from servicios import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from reservas import Reserva
from excepciones import (
    ErrorSistema,
    ClienteNoEncontrado,
    ServicioNoEncontrado,
    ReservaNoEncontrada
)
from logs import registrar_evento, registrar_error, registrar_advertencia


# Listas para almacenar la información durante la ejecución.
clientes = []
reservas = []

# Catálogo inicial de servicios.
servicios = [
    ReservaSalas(
        "S001", "Reserva de sala de reuniones",
        "Espacio para reuniones empresariales", 150000, 20
    ),
    AlquilerEquipos(
        "S002", "Alquiler de computador",
        "Alquiler de equipo tecnológico", 80000,
        "Computador portátil"
    ),
    AsesoriaEspecializada(
        "S003", "Asesoría tecnológica",
        "Orientación para proyectos tecnológicos", 200000,
        "Tecnología y software"
    )
]



def registrar_cliente():
    """Permite registrar un nuevo cliente."""

    print("\n--- REGISTRO DE CLIENTE ---")

    try:
        identificador = f"C{len(clientes) + 1:03d}"
        nombre = input("Nombre completo: ")
        documento = input("Documento: ")
        correo = input("Correo electrónico: ")
        telefono = input("Teléfono: ")

        cliente = Cliente(
            identificador, nombre, documento, correo, telefono
        )

    except (ValueError, TypeError) as error:
        print(f"Error al registrar el cliente: {error}")
        registrar_error(f"Error al registrar cliente: {error}")

    else:
        clientes.append(cliente)

        print("\nCliente registrado correctamente.")
        print(cliente)

        registrar_evento(f"Cliente registrado: {identificador}")

    finally:
        print("\nFinalizó el proceso de registro de cliente.")



def mostrar_servicios():
    """Muestra el catálogo de servicios disponibles."""

    print("\n--- SERVICIOS DISPONIBLES ---")

    for i, servicio in enumerate(servicios, start=1):
        print(f"{i}. {servicio}")
        print(servicio.procesar())
        print("-" * 50)


def crear_reserva():
    """Permite crear una reserva para un cliente."""

    try:
        if not clientes:
            raise ClienteNoEncontrado(
                "Primero debe registrar un cliente."
            )

        print("\n--- CLIENTES REGISTRADOS ---")
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. {cliente.nombre}")

        opcion_cliente = int(input("Seleccione el número del cliente: "))

        if opcion_cliente < 1 or opcion_cliente > len(clientes):
            raise ClienteNoEncontrado("El cliente seleccionado no existe.")

        cliente = clientes[opcion_cliente - 1]

        mostrar_servicios()

        opcion_servicio = int(input("Seleccione el número del servicio: "))

        if opcion_servicio < 1 or opcion_servicio > len(servicios):
            raise ServicioNoEncontrado("El servicio seleccionado no existe.")

        servicio = servicios[opcion_servicio - 1]

        identificador = f"R{len(reservas) + 1:03d}"
        fecha = input("Fecha (DD/MM/AAAA): ")
        hora = input("Hora (HH:MM): ")
        duracion = float(input("Duración en horas: "))

        reserva = Reserva(
            identificador, cliente, servicio,
            fecha, hora, duracion
        )

        reservas.append(reserva)

        print("\nReserva creada correctamente.")
        print(reserva)
        registrar_evento(f"Reserva creada: {identificador}")

    except (ValueError, TypeError, ErrorSistema) as error:
        print(f"Error al crear la reserva: {error}")
        registrar_error(f"Error al crear reserva: {error}")


def mostrar_reservas():
    """Muestra las reservas registradas."""

    print("\n--- RESERVAS REGISTRADAS ---")

    if not reservas:
        print("No hay reservas registradas.")
        return

    for reserva in reservas:
        print(reserva)
        print("-" * 50)


def buscar_reserva():
    """Busca una reserva por su identificador."""

    identificador = input("Ingrese el código de la reserva: ")

    for reserva in reservas:
        if reserva.identificador == identificador:
            return reserva

    raise ReservaNoEncontrada(
        f"No se encontró la reserva {identificador}."
    )


def gestionar_reserva(accion):
    """Permite confirmar, cancelar o procesar una reserva."""

    try:
        reserva = buscar_reserva()

        if accion == "confirmar":
            mensaje = reserva.confirmar()
        elif accion == "cancelar":
            mensaje = reserva.cancelar()
        elif accion == "procesar":
            mensaje = reserva.procesar()

        print(mensaje)
        print(reserva)

        registrar_evento(
            f"Reserva {reserva.identificador}: acción {accion}"
        )

    except (ErrorSistema, ValueError, TypeError) as error:
        print(f"No se pudo realizar la operación: {error}")
        registrar_error(f"Error al gestionar reserva: {error}")


def iniciar_sistema():
    """Función principal para iniciar la aplicación."""

    print("=" * 55)
    print("       SISTEMA INTEGRAL DE GESTIÓN SOFTWARE FJ")
    print("=" * 55)
    print("Bienvenido al sistema de gestión.")

    registrar_evento("Sistema Software FJ iniciado.")

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Registrar cliente")
        print("2. Consultar servicios")
        print("3. Crear reserva")
        print("4. Mostrar reservas")
        print("5. Confirmar reserva")
        print("6. Cancelar reserva")
        print("7. Procesar reserva")
        print("0. Salir")

        try:
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                registrar_cliente()
            elif opcion == "2":
                mostrar_servicios()
            elif opcion == "3":
                crear_reserva()
            elif opcion == "4":
                print("\nESTOY ENTRANDO A LA OPCIÓN 4")
                mostrar_reservas()
                input("\nPresione Enter para continuar...")
            elif opcion == "5":
                gestionar_reserva("confirmar")

            elif opcion == "6":
                gestionar_reserva("cancelar")

            elif opcion == "7":
                gestionar_reserva("procesar")

            elif opcion == "0":
                registrar_evento("Sistema Software FJ finalizado.")
                print("\nGracias por utilizar Software FJ.")
                break
            else:
                registrar_advertencia(
                    f"Opción no válida: {opcion}"
                )
                print("Opción no válida. Intente nuevamente.")

        except (ValueError, TypeError) as error:
            registrar_error(f"Error en el menú principal: {error}")
            print(f"Se presentó un error: {error}")


if __name__ == "__main__":
    iniciar_sistema()

