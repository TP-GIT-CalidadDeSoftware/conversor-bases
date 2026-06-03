"""Conversión entre binario y hexadecimal."""

import string


def binary_to_hex(value: str) -> str:
    """Convierte un número binario (cadena) a hexadecimal (cadena).

    Args:
        value: Cadena con el número binario (ej: "11111111").

    Returns:
        Cadena con el número hexadecimal equivalente en mayúsculas (ej: "FF").

    Raises:
        ValueError: Si la cadena no representa un binario válido.
    """
    normalized = value.strip()
    if not normalized or any(ch not in "01" for ch in normalized):
        raise ValueError(f"'{value}' no es un binario válido")
    return format(int(normalized, 2), "X")


def hex_to_binary(value: str) -> str:
    """Convierte un número hexadecimal (cadena) a binario (cadena).

    Args:
        value: Cadena con el número hexadecimal (ej: "FF").

    Returns:
        Cadena con el número binario equivalente (ej: "11111111").

    Raises:
        ValueError: Si la cadena no representa un hexadecimal válido.
    """
    normalized = value.strip()
    if not normalized or any(ch not in string.hexdigits for ch in normalized):
        raise ValueError(f"'{value}' no es un hexadecimal válido")
    return format(int(normalized, 16), "b")
