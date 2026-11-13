
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que establece la estructura general
    de las entidades del Sistema Software FJ.

    Las clases que hereden de Entidad deberán implementar
    su propio método de validación.
    """

    def __init__(self, identificador):
        self.__identificador = None
        self.identificador = identificador

    @property
    def identificador(self):
        """Permite consultar el identificador."""
        return self.__identificador

    @identificador.setter
    def identificador(self, valor):
        """
        Valida y asigna el identificador.
        Se utiliza una cadena para conservar formatos
        como los identificadores que comienzan en cero.
        """
        if not isinstance(valor, str):
            raise TypeError(
                "El identificador debe ser una cadena de texto."
            )

        valor = valor.strip()

        if not valor:
            raise ValueError(
                "El identificador no puede estar vacío."
            )

        self.__identificador = valor

    @abstractmethod
    def validar(self):
        """
        Método abstracto que cada clase hija debe implementar.
        """
        pass

    def __str__(self):
        """Representación general de la entidad."""
        return f"Entidad: {self.identificador}"



