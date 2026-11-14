
import unittest
from decimal import Decimal

from reservas import Reserva
from clientes import Cliente
from servicios import ReservaEspacio, AlquilerEquipo, Consultoria
from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    EstadoReservaInvalido
)


class TestReserva(unittest.TestCase):
    def test_procesar_reserva_con_impuesto_descuento(self):
        self.reserva.confirmar()

        costo = self.reserva.procesar(
            impuesto=19,
            descuento=10
        )

        self.assertEqual(costo, Decimal("214200.00"))
        self.assertEqual(self.reserva.estado, "Procesada")

    def setUp(self):
        self.cliente = Cliente(
            "CLI001",
            "Harvey",
            "Poveda",
            "harvey@example.com",
            "3001234567"
        )

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
            "Orientación informática.",
            80000,
            "Tecnología"
        )

        self.reserva = Reserva(
            "RES001",
            self.cliente,
            self.espacio,
            2
        )

    def test_creacion_correcta(self):
        self.assertEqual(self.reserva.identificador, "RES001")
        self.assertEqual(self.reserva.cliente, self.cliente)
        self.assertEqual(self.reserva.servicio, self.espacio)
        self.assertEqual(self.reserva.duracion, Decimal("2"))
        self.assertEqual(self.reserva.estado, "Pendiente")

    def test_reserva_es_una_entidad_valida(self):
        self.assertTrue(self.reserva.validar())

    def test_cliente_invalido(self):
        with self.assertRaises(ErrorCliente):
            Reserva("RES002", "Cliente incorrecto", self.espacio, 2)

    def test_servicio_invalido(self):
        with self.assertRaises(ErrorServicio):
            Reserva("RES003", self.cliente, "Servicio incorrecto", 2)

    def test_duracion_cero(self):
        with self.assertRaises(ValueError):
            Reserva("RES004", self.cliente, self.espacio, 0)

    def test_duracion_negativa(self):
        with self.assertRaises(ValueError):
            Reserva("RES005", self.cliente, self.espacio, -2)

    def test_duracion_no_numerica(self):
        with self.assertRaises(TypeError):
            Reserva("RES006", self.cliente, self.espacio, "dos")

    def test_calcular_costo_espacio(self):
        costo = self.reserva.calcular_costo()

        self.assertEqual(costo, Decimal("200000.00"))

    def test_calcular_costo_equipo(self):
        reserva = Reserva(
            "RES007",
            self.cliente,
            self.equipo,
            3
        )

        self.assertEqual(
            reserva.calcular_costo(),
            Decimal("150000.00")
        )

    def test_calcular_costo_consultoria(self):
        reserva = Reserva(
            "RES008",
            self.cliente,
            self.consultoria,
            2
        )
        self.assertEqual(
            reserva.calcular_costo(),
            Decimal("160000.00")
        )

    def test_calcular_costo_con_impuesto_descuento(self):
        costo = self.reserva.calcular_costo(
            impuesto=19,
            descuento=10
        )

        self.assertEqual(costo, Decimal("214200.00"))

    def test_confirmar_reserva(self):
        resultado = self.reserva.confirmar()

        self.assertTrue(resultado)
        self.assertEqual(self.reserva.estado, "Confirmada")

    def test_no_confirmar_dos_veces(self):
        self.reserva.confirmar()

        with self.assertRaises(EstadoReservaInvalido):
            self.reserva.confirmar()

    def test_cancelar_reserva_pendiente(self):
        self.assertTrue(self.reserva.cancelar())
        self.assertEqual(self.reserva.estado, "Cancelada")

    def test_cancelar_reserva_confirmada(self):
        self.reserva.confirmar()
        self.reserva.cancelar()

        self.assertEqual(self.reserva.estado, "Cancelada")

    def test_no_cancelar_reserva_procesada(self):
        self.reserva.confirmar()
        self.reserva.procesar()

        with self.assertRaises(EstadoReservaInvalido):
            self.reserva.cancelar()

    def test_no_calcular_reserva_cancelada(self):
        self.reserva.cancelar()

        with self.assertRaises(EstadoReservaInvalido):
            self.reserva.calcular_costo()

    def test_procesar_reserva(self):
        self.reserva.confirmar()

        costo = self.reserva.procesar()

        self.assertEqual(costo, Decimal("200000.00"))
        self.assertEqual(self.reserva.estado, "Procesada")

    def test_no_procesar_reserva_pendiente(self):
        with self.assertRaises(EstadoReservaInvalido):
            self.reserva.procesar()

    def test_no_procesar_dos_veces(self):
        self.reserva.confirmar()
        self.reserva.procesar()

        with self.assertRaises(EstadoReservaInvalido):
            self.reserva.procesar()

    def test_representacion_textual(self):
        resultado = str(self.reserva)

        self.assertIn("RES001", resultado)
        self.assertIn("Harvey", resultado)
        self.assertIn("Sala principal", resultado)


if __name__ == "__main__":
    unittest.main()
def test_procesar_reserva_con_impuesto_descuento(self):
    self.reserva.confirmar()

    costo = self.reserva.procesar(
        impuesto=19,
        descuento=10
    )

    self.assertEqual(costo, Decimal("214200.00"))
    self.assertEqual(self.reserva.estado, "Procesada")
