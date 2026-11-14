
from decimal import Decimal, InvalidOperation

from entidades import Entidad
from clientes import Cliente
from servicios import Servicio

from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    EstadoReservaInvalido
)

from logs import registrar_evento, registrar_error


class Reserva(Entidad):
    """
    Representa una reserva realizada por un cliente
    para utilizar uno de los servicios de Software FJ.
    """

    ESTADOS = (
        "Pendiente",
        "Confirmada",
        "Procesada",
        "Cancelada"
    )

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)

        if not isinstance(cliente, Cliente):
            raise ErrorCliente(
                "La reserva debe estar asociada a un cliente válido."
            )

        if not isinstance(servicio, Servicio):
            raise ErrorServicio(
                "La reserva debe estar asociada a un servicio válido."
            )

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = self.__validar_duracion(duracion)
        self.__estado = "Pendiente"

        self.validar()

        registrar_evento(
            f"Reserva {self.identificador} creada para el cliente "
            f"{self.cliente.identificador}."
        )

    @staticmethod
    def __validar_duracion(valor):
        """Valida que la duración sea un número positivo y finito."""

        if isinstance(valor, bool):
            raise TypeError("La duración debe ser numérica.")

        try:
            duracion = Decimal(str(valor))
        except (InvalidOperation, ValueError):
            raise TypeError("La duración debe ser un número válido.")

        if not duracion.is_finite():
            raise ValueError("La duración debe ser un número finito.")

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        return duracion

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def validar(self):
        """Comprueba que los datos de la reserva sean válidos."""

        if not isinstance(self.cliente, Cliente):
            raise ErrorCliente(
                "El cliente de la reserva no es válido."
            )

        if not isinstance(self.servicio, Servicio):
            raise ErrorServicio(
                "El servicio de la reserva no es válido."
            )

        self.__validar_duracion(self.duracion)

        return True

    def calcular_costo(self, impuesto=0, descuento=0):
        """
        Calcula el costo de la reserva utilizando
        el método polimórfico del servicio asociado.
        """

        if self.estado == "Cancelada":
            raise EstadoReservaInvalido(
                "No se puede calcular el costo de una reserva cancelada."
            )

        try:
            return self.servicio.calcular_costo(
                cantidad=self.duracion,
                impuesto=impuesto,
                descuento=descuento
            )

        except (TypeError, ValueError) as error:
            registrar_error(
                f"Error al calcular el costo de la reserva "
                f"{self.identificador}: {error}"
            )

            raise ErrorReserva(
                "No fue posible calcular el costo de la reserva."
            ) from error

    def confirmar(self):
        """Confirma una reserva que se encuentra pendiente."""

        if self.estado != "Pendiente":
            raise EstadoReservaInvalido(
                f"No se puede confirmar una reserva en estado "
                f"{self.estado}."
            )

        self.__estado = "Confirmada"

        registrar_evento(
            f"Reserva {self.identificador} confirmada."
        )

        return True

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.estado not in ("Pendiente", "Confirmada"):
            raise EstadoReservaInvalido(
                f"No se puede cancelar una reserva en estado "
                f"{self.estado}."
            )

        self.__estado = "Cancelada"

        registrar_evento(
            f"Reserva {self.identificador} cancelada."
        )

        return True

    def procesar(self, impuesto=0, descuento=0):
        """
        Procesa una reserva confirmada.
        Calcula el costo aplicando el impuesto y descuento indicados.
        """

        if self.estado != "Confirmada":
            raise EstadoReservaInvalido(
                "Solamente se pueden procesar reservas confirmadas."
            )

        try:
            costo = self.calcular_costo(
                impuesto=impuesto,
                descuento=descuento
            )

            self.__estado = "Procesada"

            registrar_evento(
                f"Reserva {self.identificador} procesada. "
                f"Costo total: {costo}."
            )

            return costo

        except ErrorReserva as error:
            registrar_error(
                f"No se pudo procesar la reserva "
                f"{self.identificador}: {error}"
            )
            raise

    def __str__(self):
        """Devuelve un resumen de la reserva."""

        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} "
            f"{self.cliente.apellido} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion} | "
            f"Estado: {self.estado}"
        )
