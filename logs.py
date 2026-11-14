
import logging
from pathlib import Path

# Archivo donde se guardarán los registros
RUTA_LOG = Path(__file__).with_name("software_fj.log")

logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)

def registrar_evento(mensaje):
    """Registra una operación realizada correctamente."""
    logging.info(mensaje)

def registrar_error(mensaje):
    """Registra un error ocurrido en el sistema."""
    logging.error(mensaje)

def registrar_advertencia(mensaje):
    """Registra una situación que requiere atención."""
    logging.warning(mensaje)


if __name__ == "__main__":
    registrar_evento("Prueba de registro de eventos.")
    registrar_advertencia("Prueba de advertencia.")
    registrar_error("Prueba de registro de errores.")
    print("Prueba de registros realizada correctamente.")
    print(f"Archivo generado: {RUTA_LOG}")

