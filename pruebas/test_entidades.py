
import unittest

from entidades import Entidad


class EntidadPrueba(Entidad):
    """Clase concreta utilizada únicamente para probar Entidad."""

    def validar(self) -> bool:
        return True


class TestEntidad(unittest.TestCase):

    def test_identificador_valido(self):
        entidad = EntidadPrueba("CLI-001")
        self.assertEqual(entidad.identificador, "CLI-001")

    def test_identificador_vacio(self):
        with self.assertRaises(ValueError):
            EntidadPrueba("   ")

    def test_identificador_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            EntidadPrueba(123)

    def test_no_se_puede_instanciar_entidad(self):
        with self.assertRaises(TypeError):
            Entidad("GEN-001")

    def test_validacion_de_entidad_derivada(self):
        entidad = EntidadPrueba("CLI-002")
        self.assertTrue(entidad.validar())


if __name__ == "__main__":
    unittest.main()
