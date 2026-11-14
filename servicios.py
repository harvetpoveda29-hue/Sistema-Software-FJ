from abc import abstractmethod
from entidades import Entidad


class Servicio(Entidad):
    """
    Clase abstracta que representa los servicios de Software FJ.
    Contiene los datos comunes de todos los servicios.
    """

    def __init__(self, identificador, nombre, descripcion, precio):
        super().__init__(identificador)

        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio

        self.validar()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio(self):
        return self.__precio

    def validar(self):
        """Valida los datos generales del servicio."""

        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if not isinstance(self.__descripcion, str) or not self.__descripcion.strip():
            raise ValueError("La descripción es obligatoria.")

        if isinstance(self.__precio, bool) or not isinstance(self.__precio, (int, float)):
            raise TypeError("El precio debe ser numérico.")

        if self.__precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        return True

    def procesar(self):
        """
        Método abstracto que cada servicio especializado
        debe implementar de manera diferente.
        """
        pass

    def __str__(self):
        return (
            f"{self.__class__.__name__}: {self.nombre} | "
            f"Descripción: {self.descripcion} | "
            f"Precio: ${self.precio:,.2f}"
        )
    def consultar(self, dato=None):
        """Permite consultar toda la información o un dato específico."""

        if dato is None:
            return str(self)

        if dato == "nombre":
            return self.nombre

        elif dato == "precio":
            return self.precio

        elif dato == "descripcion":
            return self.descripcion

        else:
            raise ValueError("El dato solicitado no existe.")

class ReservaSalas(Servicio):
    """Servicio especializado en reservas de salas."""


    def __init__(self, identificador, nombre, descripcion, precio, capacidad):
        super().__init__(identificador, nombre, descripcion, precio)
        self.__capacidad = capacidad

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo.")

    @property
    def capacidad(self):
        return self.__capacidad

    def procesar(self):
        return (
            f"Procesando reserva de sala: {self.nombre}. "
            f"Capacidad: {self.capacidad} personas."
        )


class AlquilerEquipos(Servicio):
    """Servicio especializado en alquiler de equipos."""

    def __init__(self, identificador, nombre, descripcion, precio, equipo):
        super().__init__(identificador, nombre, descripcion, precio)
        self.__equipo = equipo

        if not isinstance(equipo, str) or not equipo.strip():
            raise ValueError("Debe especificar el equipo que se alquilará.")

    @property
    def equipo(self):
        return self.__equipo

    def procesar(self):
        return (
            f"Procesando alquiler del equipo: {self.equipo}. "
            f"Servicio: {self.nombre}."
        )


class AsesoriaEspecializada(Servicio):
    """Servicio especializado en asesorías profesionales."""

    def __init__(self, identificador, nombre, descripcion, precio, especialidad):
        super().__init__(identificador, nombre, descripcion, precio)
        self.__especialidad = especialidad

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("Debe indicar la especialidad de la asesoría.")

    @property
    def especialidad(self):
        return self.__especialidad

    def procesar(self):
        return (
            f"Procesando asesoría especializada en: "
            f"{self.especialidad}."
        )


# Prueba de los tres servicios especializados
if __name__ == "__main__":

    sala = ReservaSalas(
        "S001",
        "Reserva de sala de reuniones",
        "Espacio para reuniones empresariales",
        150000,
        20
    )

    equipo = AlquilerEquipos(
        "S002",
        "Alquiler de computador",
        "Alquiler de equipo tecnológico",
        80000,
        "Computador portátil"
    )

    asesoria = AsesoriaEspecializada(
        "S003",
        "Asesoría tecnológica",
        "Orientación para proyectos tecnológicos",
        200000,
        "Tecnología y software"
    )

    servicios = [sala, equipo, asesoria]

    for servicio in servicios:
        print(servicio)
        print(servicio.procesar())
        print("-" * 50)

    print("\nPRUEBA DE SOBRECARGA DE MÉTODOS")

    print("Consulta completa:")
    print(sala.consultar())

    print("\nConsulta del nombre:")
    print(sala.consultar("nombre"))

    print("\nConsulta del precio:")
    print(sala.consultar("precio"))
