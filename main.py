
"""
Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Curso: Programación
Universidad Nacional Abierta y a Distancia
Fase 4
"""

from clientes import Cliente

from servicios import (
    ReservaEspacio,
    AlquilerEquipo,
    Consultoria
)

from reservas import Reserva

from excepciones import (
    ErrorReserva,
    EstadoReservaInvalido
)

from logs import registrar_evento, registrar_error


def mostrar_titulo(mensaje):
    """Muestra los títulos de las operaciones."""
    print("\n" + "=" * 60)
    print(mensaje)
    print("=" * 60)


def iniciar_sistema():
    """Ejecuta las operaciones de demostración del sistema."""

    print("=" * 60)
    print("          SISTEMA INTEGRAL SOFTWARE FJ")
    print("       Gestión de Clientes, Servicios y Reservas")
    print("=" * 60)

    clientes = []
    servicios = []
    reservas = []

    # --------------------------------------------------
    # OPERACIÓN 1: Registrar un cliente correctamente.
    # Demuestra try, except, else y finally.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 1: REGISTRO DE CLIENTE")

    try:
        cliente1 = Cliente(
            "CLI001",
            "Harvey",
            "Poveda",
            "harvey@example.com",
            "3001234567"
        )

        clientes.append(cliente1)

    except (TypeError, ValueError) as error:
        registrar_error(f"Error registrando cliente: {error}")
        print(f"Error: {error}")

    else:
        registrar_evento(
            f"Cliente {cliente1.identificador} registrado correctamente."
        )
        print("Cliente registrado correctamente.")
        print(cliente1)

    finally:
        print("Finalizó la operación de registro.")

    # --------------------------------------------------
    # OPERACIÓN 2: Registrar un segundo cliente.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 2: REGISTRO DE SEGUNDO CLIENTE")

    try:
        cliente2 = Cliente(
            "CLI002",
            "Laura",
            "Gomez",
            "laura@example.com",
            "3109876543"
        )

        clientes.append(cliente2)

        registrar_evento(
            f"Cliente {cliente2.identificador} registrado correctamente."
        )

        print("Segundo cliente registrado.")
        print(cliente2)

    except (TypeError, ValueError) as error:
        registrar_error(f"Error registrando segundo cliente: {error}")
        print(f"Error: {error}")

    # --------------------------------------------------
    # OPERACIÓN 3: Intentar registrar un cliente inválido.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 3: VALIDACIÓN DE CLIENTE INVÁLIDO")

    try:
        cliente_invalido = Cliente(
            "CLI003",
            "Juan123",
            "Perez",
            "juan@example.com",
            "3001234567"
        )

        clientes.append(cliente_invalido)

    except (TypeError, ValueError) as error:
        registrar_error(f"Registro rechazado: {error}")
        print(f"El cliente no pudo registrarse: {error}")

    # --------------------------------------------------
    # OPERACIÓN 4: Crear servicio de reserva de espacios.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 4: CREACIÓN DE RESERVA DE ESPACIO")

    espacio = ReservaEspacio(
        "Sala principal",
        "Sala para reuniones y eventos.",
        100000,
        30
    )

    servicios.append(espacio)

    print("Servicio creado correctamente.")
    print(espacio.obtener_descripcion())

    # --------------------------------------------------
    # OPERACIÓN 5: Crear servicio de alquiler de equipos.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 5: CREACIÓN DE ALQUILER DE EQUIPO")

    equipo = AlquilerEquipo(
        "Proyector",
        "Proyector multimedia HD.",
        50000,
        "Audiovisual"
    )

    servicios.append(equipo)

    print("Servicio creado correctamente.")
    print(equipo.obtener_descripcion())

    # --------------------------------------------------
    # OPERACIÓN 6: Crear servicio de consultoría.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 6: CREACIÓN DE CONSULTORÍA")

    consultoria = Consultoria(
        "Asesoría tecnológica",
        "Orientación en soluciones informáticas.",
        80000,
        "Tecnología"
    )

    servicios.append(consultoria)

    print("Servicio creado correctamente.")
    print(consultoria.obtener_descripcion())

    # --------------------------------------------------
    # OPERACIÓN 7: Crear una reserva correctamente.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 7: CREACIÓN DE RESERVA")

    reserva1 = Reserva(
        "RES001",
        cliente1,
        espacio,
        2
    )

    reservas.append(reserva1)

    print("Reserva creada correctamente.")
    print(reserva1)

    # --------------------------------------------------
    # OPERACIÓN 8: Confirmar la reserva.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 8: CONFIRMACIÓN DE RESERVA")

    reserva1.confirmar()

    print("Reserva confirmada.")
    print(f"Estado actual: {reserva1.estado}")

    # --------------------------------------------------
    # OPERACIÓN 9: Calcular el costo con parámetros
    # opcionales: cantidad, impuesto y descuento.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 9: CÁLCULO DEL COSTO")

    costo = reserva1.calcular_costo(
        impuesto=19,
        descuento=10
    )

    print(f"Servicio: {reserva1.servicio.nombre}")
    print(f"Duración: {reserva1.duracion} horas")
    print(f"Impuesto: 19 %")
    print(f"Descuento: 10 %")
    print(f"Costo total: ${costo}")

    # --------------------------------------------------
    # OPERACIÓN 10: Procesar la reserva confirmada.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 10: PROCESAMIENTO DE RESERVA")

    costo_final = reserva1.procesar(
    impuesto=19,
    descuento=10
)

    print("Reserva procesada correctamente.")
    print(f"Costo final: ${costo_final}")
    print(f"Estado actual: {reserva1.estado}")

    # --------------------------------------------------
    # OPERACIÓN 11: Crear y cancelar otra reserva.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 11: CANCELACIÓN DE RESERVA")

    reserva2 = Reserva(
        "RES002",
        cliente2,
        equipo,
        3
    )

    reservas.append(reserva2)

    print("Segunda reserva creada.")
    print(reserva2)

    reserva2.cancelar()

    print("Reserva cancelada correctamente.")
    print(f"Estado actual: {reserva2.estado}")

    # --------------------------------------------------
    # OPERACIÓN 12: Intentar procesar una reserva pendiente.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 12: CONTROL DE ESTADOS")

    reserva3 = Reserva(
        "RES003",
        cliente1,
        consultoria,
        2
    )

    reservas.append(reserva3)

    try:
        reserva3.procesar()

    except EstadoReservaInvalido as error:
        registrar_error(
            f"Operación no permitida en {reserva3.identificador}: {error}"
        )
        print(f"Operación rechazada correctamente: {error}")

    # --------------------------------------------------
    # OPERACIÓN 13: Intentar crear una reserva inválida.
    # --------------------------------------------------

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

    # --------------------------------------------------
    # OPERACIÓN 14: Demostrar encadenamiento de excepciones.
    # --------------------------------------------------

    mostrar_titulo("OPERACIÓN 14: ENCADENAMIENTO DE EXCEPCIONES")

    try:
        reserva3.calcular_costo(impuesto=150)

    except ErrorReserva as error:
        registrar_error(
            f"Error encadenado en reserva {reserva3.identificador}: {error}"
        )

        print(f"Excepción principal: {error}")

        if error.__cause__ is not None:
            print(
                "Excepción original:",
                type(error.__cause__).__name__
            )
            print("Detalle original:", error.__cause__)

    # --------------------------------------------------
    # RESUMEN GENERAL DEL SISTEMA.
    # --------------------------------------------------

    mostrar_titulo("RESUMEN GENERAL DEL SISTEMA")

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios creados: {len(servicios)}")
    print(f"Reservas creadas: {len(reservas)}")

    print("\nESTADO DE LAS RESERVAS:")

    for reserva in reservas:
        print(reserva)

    registrar_evento(
        "Finalización de las operaciones de demostración."
    )

    print("\n" + "=" * 60)
    print("       EJECUCIÓN DEL SISTEMA FINALIZADA")
    print("=" * 60)


# Punto de entrada de la aplicación.
if __name__ == "__main__":
    iniciar_sistema()

