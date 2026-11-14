
from datetime import datetime
from entidades import Entidad
from clientes import Cliente
from servicios import Servicio, ReservaSalas


class Reserva(Entidad):
    """
    Representa una reserva de un cliente para un servicio
    de Software FJ.
    """

    def __init__(self, identificador, cliente, servicio, fecha, hora,
                 duracion, estado="Pendiente"):
        super().__init__(identificador)

        self.__cliente = cliente
        self.__servicio = servicio
        self.__fecha = fecha
        self.__hora = hora
        self.__duracion = duracion
        self.__estado = estado

        self.validar()

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def fecha(self):
        return self.__fecha

    @property
    def hora(self):
        return self.__hora

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def validar(self):
        """Comprueba que los datos de la reserva sean correctos."""

        if not isinstance(self.__cliente, Cliente):
            raise TypeError("Debe seleccionar un cliente válido.")

        if not isinstance(self.__servicio, Servicio):
            raise TypeError("Debe seleccionar un servicio válido.")

        if not isinstance(self.__fecha, str):
            raise TypeError("La fecha debe ser texto.")

        try:
            datetime.strptime(self.__fecha, "%d/%m/%Y")
        except ValueError as error:
            raise ValueError(
                "La fecha debe tener el formato DD/MM/AAAA."
            ) from error

        if not isinstance(self.__hora, str):
            raise TypeError("La hora debe ser texto.")

        try:
            datetime.strptime(self.__hora, "%H:%M")
        except ValueError as error:
            raise ValueError(
                "La hora debe tener el formato HH:MM."
            ) from error

        if (isinstance(self.__duracion, bool)
                or not isinstance(self.__duracion, (int, float))
                or self.__duracion <= 0):
            raise ValueError("La duración debe ser un número positivo.")

        estados_validos = [
            "Pendiente", "Confirmada", "Cancelada", "Procesada"
        ]

        if self.__estado not in estados_validos:
            raise ValueError("El estado de la reserva no es válido.")

        return True

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.__estado != "Pendiente":
            raise ValueError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"
        return "La reserva fue confirmada correctamente."

    def cancelar(self):
        """Cancela una reserva que todavía no ha sido procesada."""

        if self.__estado in ["Cancelada", "Procesada"]:
            raise ValueError(
                "La reserva ya está cancelada o fue procesada."
            )

        self.__estado = "Cancelada"
        return "La reserva fue cancelada correctamente."

    def procesar(self):
        """Procesa el servicio cuando la reserva está confirmada."""

        if self.__estado != "Confirmada":
            raise ValueError(
                "Solo se pueden procesar reservas confirmadas."
            )

        resultado = self.__servicio.procesar()
        self.__estado = "Procesada"

        return resultado

    def __str__(self):
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Fecha: {self.fecha} | "
            f"Hora: {self.hora} | "
            f"Duración: {self.duracion} horas | "
            f"Estado: {self.estado}"
        )


# Prueba del funcionamiento de las reservas
if __name__ == "__main__":

    cliente = Cliente(
        "C001",
        "María Pérez",
        "123456789",
        "maria@gmail.com",
        "3101234567"
    )

    servicio = ReservaSalas(
        "S001",
        "Reserva de sala de reuniones",
        "Espacio para reuniones empresariales",
        150000,
        20
    )

    reserva = Reserva(
        "R001",
        cliente,
        servicio,
        "20/11/2026",
        "10:00",
        2
    )

    print(reserva)
    print(reserva.confirmar())
    print(reserva)
    print(reserva.procesar())
    print(reserva)


