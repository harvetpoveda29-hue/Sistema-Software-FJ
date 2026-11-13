
# Importamos las herramientas necesarias para crear una clase abstracta.
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa las entidades generales
    del sistema Software FJ.
    """

    def __init__(self, identificador):
        # Validamos que el identificador no esté vacío.
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        # Encapsulamos el identificador.
        self.__identificador = identificador

    @property
    def identificador(self):
        """Permite consultar el identificador."""
        return self.__identificador

    @abstractmethod
    def validar(self):
        """Método que deben implementar las clases derivadas."""
        pass

