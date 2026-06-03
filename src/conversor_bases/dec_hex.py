"""Conversión entre decimal y hexadecimal."""


def decimal_to_hex(value: str) -> str:
    """Convierte un número decimal (cadena) a hexadecimal (cadena).

    Args:
        value: Cadena con el número decimal (ej: "255").

    Returns:
        Cadena con el número hexadecimal equivalente en mayúsculas (ej: "FF").

    Raises:
        ValueError: Si la cadena no representa un decimal válido.
    """
    raise NotImplementedError("dec-hex pendiente de implementación")


def hex_to_decimal(value: str) -> str:
    """Convierte un número hexadecimal (cadena) a decimal (cadena).

    Args:
        value: Cadena con el número hexadecimal (ej: "FF").

    Returns:
        Cadena con el número decimal equivalente (ej: "255").

    Raises:
        ValueError: Si la cadena no representa un hexadecimal válido.
    """
    raise NotImplementedError("hex-dec pendiente de implementación")
