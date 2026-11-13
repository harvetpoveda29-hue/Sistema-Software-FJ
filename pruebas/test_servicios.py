
import unittest
from decimal import Decimal

from servicios import (
    Servicio,
    ReservaEspacio,
    AlquilerEquipo,
    Consultoria
)


class TestServicios(unittest.TestCase):

    def setUp(self):
        self.espacio = ReservaEspacio(
            "Sala principal",
            "Sala para reuniones y eventos.",
            100000,
            30
        )

        self.equipo = AlquilerEquipo(
            "Proyector",
            "Proyector multimedia HD.",
            50000,
            "Audiovisual"
        )

        self.consultoria = Consultoria(
            "Asesoría tecnológica",
            "Orientación en soluciones informáticas.",
            80000,
            "Tecnología"
        )

    def test_servicio_es_abstracto(self):
        with self.assertRaises(TypeError):
            Servicio("Servicio", "Descripción", 10000)

    def test_creacion_reserva_espacio(self):
        self.assertEqual(self.espacio.nombre, "Sala principal")
        self.assertEqual(self.espacio.capacidad_personas, 30)

    def test_creacion_alquiler_equipo(self):
        self.assertEqual(self.equipo.categoria, "Audiovisual")

    def test_creacion_consultoria(self):
        self.assertEqual(self.consultoria.especialidad, "Tecnología")

    def test_costo_reserva_espacio(self):
        resultado = self.espacio.calcular_costo(cantidad=2)

        self.assertEqual(resultado, Decimal("200000.00"))

    def test_costo_alquiler_equipo(self):
        resultado = self.equipo.calcular_costo(cantidad=3)

        self.assertEqual(resultado, Decimal("150000.00"))

    def test_costo_consultoria(self):
        resultado = self.consultoria.calcular_costo(cantidad=2)

        self.assertEqual(resultado, Decimal("160000.00"))

    def test_costo_con_impuesto_y_descuento(self):
        resultado = self.espacio.calcular_costo(
            cantidad=3,
            impuesto=19,
            descuento=10
        )

        self.assertEqual(resultado, Decimal("321300.00"))

    def test_cantidad_invalida(self):
        with self.assertRaises(ValueError):
            self.espacio.calcular_costo(cantidad=0)

    def test_impuesto_invalido(self):
        with self.assertRaises(ValueError):
            self.espacio.calcular_costo(impuesto=120)

    def test_descuento_invalido(self):
        with self.assertRaises(ValueError):
            self.equipo.calcular_costo(descuento=110)

    def test_capacidad_invalida(self):
        with self.assertRaises(ValueError):
            ReservaEspacio(
                "Sala",
                "Espacio de reuniones",
                100000,
                0
            )

    def test_descripcion_polimorfica(self):
        servicios = [
            self.espacio,
            self.equipo,
            self.consultoria
        ]

        for servicio in servicios:
            with self.subTest(servicio=servicio.nombre):
                self.assertIsInstance(
                    servicio.obtener_descripcion(), str
                )
                self.assertTrue(servicio.obtener_descripcion())


if __name__ == "__main__":
    unittest.main()

