from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta base para las entidades del sistema Software FJ.

    Centraliza el identificador y establece el método de validación
    que deben implementar las clases derivadas.
    """

    def __init__(self, identificador: str):
        """
        Inicializa una entidad con un identificador obligatorio.

        Args:
            identificador: Código único que identifica la entidad.

        Raises:
            TypeError: Si el identificador no es una cadena.
            ValueError: Si el identificador está vacío.
        """

        if not isinstance(identificador, str):
            raise TypeError("El identificador debe ser una cadena de texto.")

        identificador = identificador.strip()

        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        self.__identificador = identificador

    @property
    def identificador(self) -> str:
        """Permite consultar el identificador sin modificarlo directamente."""
        return self.__identificador

    @abstractmethod
    def validar(self) -> bool:
        """
        Define las validaciones obligatorias de cada entidad derivada.

        Cada clase hija debe implementar este método.
        """
        pass

    def __str__(self) -> str:
        """Representación legible de la entidad."""
        return f"{self.__class__.__name__}: {self.identificador}"

    def __repr__(self) -> str:
        """Representación técnica de la entidad."""
        return (
            f"{self.__class__.__name__}"
            f"(identificador={self.identificador!r})"
        )


