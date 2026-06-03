"""Conversión entre decimal y hexadecimal."""

_HEX_DIGITS = "0123456789abcdefABCDEF"


def decimal_to_hex(value: str) -> str:
    """Convierte un número decimal (cadena) a hexadecimal (cadena).

    Args:
        value: Cadena con el número decimal (ej: "255").

    Returns:
        Cadena con el número hexadecimal equivalente en mayúsculas (ej: "FF").

    Raises:
        ValueError: Si la cadena no representa un decimal válido.
    """
    if not value.isdigit():
        raise ValueError(f"'{value}' no es un decimal válido")
    return format(int(value), "X")


def hex_to_decimal(value: str) -> str:
    """Convierte un número hexadecimal (cadena) a decimal (cadena).

    Args:
        value: Cadena con el número hexadecimal (ej: "FF"). Acepta mayúsculas
            y minúsculas.

    Returns:
        Cadena con el número decimal equivalente (ej: "255").

    Raises:
        ValueError: Si la cadena no representa un hexadecimal válido.
    """
    if not value or any(c not in _HEX_DIGITS for c in value):
        raise ValueError(f"'{value}' no es un hexadecimal válido")
    return str(int(value, 16))
