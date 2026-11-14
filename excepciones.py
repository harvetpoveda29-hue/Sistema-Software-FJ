
class ErrorSistema(Exception):
    """Excepción base para los errores del sistema Software FJ."""
    pass


class ErrorValidacion(ErrorSistema):
    """Se presenta cuando los datos ingresados no son válidos."""
    pass


class ClienteNoEncontrado(ErrorSistema):
    """Se presenta cuando no se encuentra un cliente."""
    pass


class ServicioNoEncontrado(ErrorSistema):
    """Se presenta cuando no se encuentra un servicio."""
    pass


class ReservaNoEncontrada(ErrorSistema):
    """Se presenta cuando no se encuentra una reserva."""
    pass


class ErrorReserva(ErrorSistema):
    """Se presenta cuando una operación de reserva no puede realizarse."""
    pass


