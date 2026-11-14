
import logging
from pathlib import Path


# Directorio donde se almacenarán los registros.
DIRECTORIO_LOGS = Path("registros")

# Crear el directorio si todavía no existe.
DIRECTORIO_LOGS.mkdir(exist_ok=True)

# Configuración del archivo de registro.
RUTA_LOG = DIRECTORIO_LOGS / "sistema.log"

logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)

# Evitar agregar manejadores repetidos.
if not logger.handlers:
    manejador = logging.FileHandler(
        RUTA_LOG,
        encoding="utf-8"
    )

    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    manejador.setFormatter(formato)
    logger.addHandler(manejador)


def registrar_evento(mensaje):
    """Registra una operación importante del sistema."""
    logger.info(mensaje)


def registrar_error(mensaje):
    """Registra un error ocurrido durante la ejecución."""
    logger.error(mensaje)


def registrar_excepcion(mensaje):
    """Registra un error incluyendo información de la excepción."""
    logger.exception(mensaje)

def registrar_advertencia(mensaje):
    """Registra una advertencia durante la ejecución del sistema."""
    logger.warning(mensaje)

