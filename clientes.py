
import re

from entidades import Entidad


class Cliente(Entidad):
    """
    Representa a un cliente del sistema Software FJ.

    Hereda el identificador de Entidad y administra
    los datos personales mediante atributos privados.
    """

    def __init__(self, identificador, nombre, apellido, correo, telefono):
        super().__init__(identificador)

        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__telefono = telefono

        self.validar()

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = self.__validar_nombre(valor, "nombre")

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        self.__apellido = self.__validar_nombre(valor, "apellido")

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        self.__correo = self.__validar_correo(valor)

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        self.__telefono = self.__validar_telefono(valor)

    @staticmethod
    def __validar_nombre(valor, campo):
        if not isinstance(valor, str):
            raise TypeError(f"El {campo} debe ser texto.")

        valor = valor.strip()

        if not 2 <= len(valor) <= 60:
            raise ValueError(
                f"El {campo} debe tener entre 2 y 60 caracteres."
            )

        if not any(caracter.isalpha() for caracter in valor):
            raise ValueError(f"El {campo} debe contener letras.")

        if not all(
            caracter.isalpha() or caracter in " -'’"
            for caracter in valor
        ):
            raise ValueError(
                f"El {campo} contiene caracteres no permitidos."
            )

        return valor

    @staticmethod
    def __validar_correo(valor):
        if not isinstance(valor, str):
            raise TypeError("El correo debe ser texto.")

        valor = valor.strip().lower()

        patron = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if not re.fullmatch(patron, valor):
            raise ValueError("El formato del correo no es válido.")

        return valor

    @staticmethod
    def __validar_telefono(valor):
        if not isinstance(valor, str):
            raise TypeError("El teléfono debe ser texto.")

        valor = valor.strip()

        # Permite espacios, guiones y paréntesis como separadores.
        normalizado = re.sub(r"[\s\-()]", "", valor)

        if not re.fullmatch(r"\+?\d{7,15}", normalizado):
            raise ValueError(
                "El teléfono debe contener entre 7 y 15 dígitos."
            )

        return normalizado

    def validar(self):
        """Comprueba que todos los datos del cliente sean válidos."""

        self.__validar_nombre(self.nombre, "nombre")
        self.__validar_nombre(self.apellido, "apellido")
        self.__validar_correo(self.correo)
        self.__validar_telefono(self.telefono)

        return True

    def __str__(self):
        return (
            f"Cliente: {self.nombre} {self.apellido} | "
            f"ID: {self.identificador} | "
            f"Correo: {self.correo}"
        )

