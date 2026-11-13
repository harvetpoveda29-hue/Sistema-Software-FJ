
import unittest

from entidades import Entidad


class EntidadPrueba(Entidad):
    """Clase concreta utilizada únicamente para probar Entidad."""

    def validar(self):
        return True


class TestEntidad(unittest.TestCase):

    def test_creacion_correcta(self):
        entidad = EntidadPrueba("001")
        self.assertEqual(entidad.identificador, "001")

    def test_identificador_vacio(self):
        with self.assertRaises(ValueError):
            EntidadPrueba("   ")

    def test_identificador_nulo(self):
        with self.assertRaises(TypeError):
            EntidadPrueba(None)

    def test_identificador_no_textual(self):
        with self.assertRaises(TypeError):
            EntidadPrueba(123)

    def test_entidad_es_abstracta(self):
        with self.assertRaises(TypeError):
            Entidad("001")

    def test_validacion(self):
        entidad = EntidadPrueba("001")
        self.assertTrue(entidad.validar())


if __name__ == "__main__":
    unittest.main()

