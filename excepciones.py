
class ErrorSistema(Exception):
    """Excepción base para los errores del sistema Software FJ."""
    pass


class ErrorValidacion(ErrorSistema):
    """Se produce cuando un dato no cumple las validaciones."""
    pass


class ErrorCliente(ErrorSistema):
    """Se produce cuando ocurre un problema relacionado con un cliente."""
    pass


class ErrorServicio(ErrorSistema):
    """Se produce cuando ocurre un problema relacionado con un servicio."""
    pass


class ErrorReserva(ErrorSistema):
    """Se produce cuando ocurre un problema en una reserva."""
    pass


class EstadoReservaInvalido(ErrorReserva):
    """Se produce cuando una operación no está permitida para el estado actual."""
    pass


class ReservaNoEncontrada(ErrorReserva):
    """Se produce cuando no se encuentra una reserva solicitada."""
    pass

