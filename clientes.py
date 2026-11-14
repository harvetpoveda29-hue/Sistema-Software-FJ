
from entidades import Entidad


class Cliente(Entidad):
    """Representa un cliente registrado en Software FJ."""

    def __init__(self, identificador, nombre, documento, correo, telefono):
        # Inicializa los atributos de la clase padre.
        super().__init__(identificador)

        # Guarda los datos personales mediante atributos privados.
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

        # Valida que los datos ingresados sean correctos.
        self.validar()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def validar(self):
        """Comprueba que todos los datos del cliente sean válidos."""

        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ValueError("El nombre del cliente es obligatorio.")

        if not isinstance(self.__documento, str) or not self.__documento.strip():
            raise ValueError("El documento del cliente es obligatorio.")

        if not isinstance(self.__correo, str) or "@" not in self.__correo:
            raise ValueError("El correo electrónico no es válido.")

        if not isinstance(self.__telefono, str) or not self.__telefono.isdigit():
            raise ValueError("El teléfono debe contener solamente números.")

        return True

    def __str__(self):
        """Devuelve la información básica del cliente."""
        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )

if __name__ == "__main__":
    cliente = Cliente(
        "C001",
        "María Pérez",
        "123456789",
        "maria@gmail.com",
        "3101234567"
    )

    print(cliente)
