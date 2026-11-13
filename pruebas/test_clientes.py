
import unittest

from clientes import Cliente


class TestCliente(unittest.TestCase):

    def crear_cliente(self):
        return Cliente(
            "CLI001",
            "Harvey",
            "Poveda",
            "harvey@example.com",
            "3001234567"
        )

    def test_creacion_correcta(self):
        cliente = self.crear_cliente()

        self.assertEqual(cliente.identificador, "CLI001")
        self.assertEqual(cliente.nombre, "Harvey")
        self.assertEqual(cliente.apellido, "Poveda")

    def test_nombre_invalido(self):
        with self.assertRaises(ValueError):
            Cliente(
                "CLI002",
                "Juan123",
                "Perez",
                "juan@example.com",
                "3001234567"
            )

    def test_correo_invalido(self):
        with self.assertRaises(ValueError):
            Cliente(
                "CLI003",
                "Juan",
                "Perez",
                "correo-invalido",
                "3001234567"
            )

    def test_telefono_invalido(self):
        with self.assertRaises(ValueError):
            Cliente(
                "CLI004",
                "Juan",
                "Perez",
                "juan@example.com",
                "123"
            )

    def test_modificacion_correo(self):
        cliente = self.crear_cliente()
        cliente.correo = "nuevo@example.com"

        self.assertEqual(cliente.correo, "nuevo@example.com")

    def test_modificacion_invalida(self):
        cliente = self.crear_cliente()

        with self.assertRaises(ValueError):
            cliente.correo = "correo incorrecto"

    def test_validacion(self):
        cliente = self.crear_cliente()
        self.assertTrue(cliente.validar())


if __name__ == "__main__":
    unittest.main()
