
from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


class Servicio(ABC):
    """
    Clase abstracta que define la estructura general
    de los servicios ofrecidos por Software FJ.
    """

    def __init__(self, nombre, descripcion, precio_base):
        self.__nombre = self.__validar_texto(nombre, "nombre")
        self.__descripcion = self.__validar_texto(
            descripcion, "descripción"
        )
        self.__precio_base = self.__validar_numero(
            precio_base, "precio base"
        )

        if self.__precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero.")

    @staticmethod
    def __validar_texto(valor, campo):
        """Valida que un dato de texto sea obligatorio."""

        if not isinstance(valor, str):
            raise TypeError(f"El {campo} debe ser texto.")

        valor = valor.strip()

        if not valor:
            raise ValueError(f"El {campo} es obligatorio.")

        return valor

    @staticmethod
    def __validar_numero(valor, campo):
        """Valida que un dato sea un número válido y finito."""

        if isinstance(valor, bool):
            raise TypeError(f"El {campo} debe ser numérico.")

        try:
            numero = Decimal(str(valor))
        except (InvalidOperation, ValueError):
            raise TypeError(f"El {campo} debe ser un número válido.")

        if not numero.is_finite():
            raise ValueError(f"El {campo} debe ser un número finito.")

        return numero

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio_base(self):
        return self.__precio_base

    def _calcular_total(self, cantidad, impuesto, descuento):
        """
        Calcula el costo total aplicando primero el descuento
        y posteriormente el impuesto.
        """

        cantidad = self.__validar_numero(cantidad, "cantidad")
        impuesto = self.__validar_numero(impuesto, "impuesto")
        descuento = self.__validar_numero(descuento, "descuento")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if not Decimal("0") <= impuesto <= Decimal("100"):
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        if not Decimal("0") <= descuento <= Decimal("100"):
            raise ValueError("El descuento debe estar entre 0 y 100.")

        subtotal = self.precio_base * cantidad

        valor_descuento = (
            subtotal * descuento / Decimal("100")
        )

        subtotal_con_descuento = subtotal - valor_descuento

        valor_impuesto = (
            subtotal_con_descuento * impuesto / Decimal("100")
        )

        total = subtotal_con_descuento + valor_impuesto

        return total.quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

    @abstractmethod
    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):
        """Cada servicio debe implementar su propio cálculo de costo."""
        pass

    @abstractmethod
    def obtener_descripcion(self):
        """Cada servicio debe proporcionar su descripción."""
        pass


class ReservaEspacio(Servicio):
    """Servicio de reserva de espacios o salas."""

    def __init__(
        self, nombre, descripcion, precio_base, capacidad_personas
    ):
        super().__init__(nombre, descripcion, precio_base)

        if isinstance(capacidad_personas, bool) or not isinstance(
            capacidad_personas, int
        ):
            raise TypeError("La capacidad debe ser un número entero.")

        if capacidad_personas <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")

        self.__capacidad_personas = capacidad_personas

    @property
    def capacidad_personas(self):
        return self.__capacidad_personas

    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):
        # La cantidad representa las horas de reserva.
        return self._calcular_total(cantidad, impuesto, descuento)

    def obtener_descripcion(self):
        return (
            f"Reserva de espacio: {self.nombre}. "
            f"Capacidad: {self.capacidad_personas} personas. "
            f"{self.descripcion}"
        )


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos."""

    def __init__(self, nombre, descripcion, precio_base, categoria):
        super().__init__(nombre, descripcion, precio_base)

        if not isinstance(categoria, str):
            raise TypeError("La categoría debe ser texto.")

        if not categoria.strip():
            raise ValueError("La categoría del equipo es obligatoria.")

        self.__categoria = categoria.strip()

    @property
    def categoria(self):
        return self.__categoria

    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):
        # La cantidad representa los días de alquiler.
        return self._calcular_total(cantidad, impuesto, descuento)

    def obtener_descripcion(self):
        return (
            f"Alquiler de equipo: {self.nombre}. "
            f"Categoría: {self.categoria}. "
            f"{self.descripcion}"
        )


class Consultoria(Servicio):
    """Servicio de consultoría especializada."""

    def __init__(self, nombre, descripcion, precio_base, especialidad):
        super().__init__(nombre, descripcion, precio_base)

        if not isinstance(especialidad, str):
            raise TypeError("La especialidad debe ser texto.")

        if not especialidad.strip():
            raise ValueError("La especialidad es obligatoria.")

        self.__especialidad = especialidad.strip()

    @property
    def especialidad(self):
        return self.__especialidad

    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):
        # La cantidad representa las horas de consultoría.
        return self._calcular_total(cantidad, impuesto, descuento)

    def obtener_descripcion(self):
        return (
            f"Consultoría: {self.nombre}. "
            f"Especialidad: {self.especialidad}. "
            f"{self.descripcion}"
        )
