"""Conversión entre binario y hexadecimal."""


def binary_to_hex(value: str) -> str:
    """Convierte un número binario (cadena) a hexadecimal (cadena).

    Args:
        value: Cadena con el número binario (ej: "11111111").

    Returns:
        Cadena con el número hexadecimal equivalente en mayúsculas (ej: "FF").

    Raises:
        ValueError: Si la cadena no representa un binario válido.
    """
    raise NotImplementedError("bin-hex pendiente de implementación")


def hex_to_binary(value: str) -> str:
    """Convierte un número hexadecimal (cadena) a binario (cadena).

    Args:
        value: Cadena con el número hexadecimal (ej: "FF").

    Returns:
        Cadena con el número binario equivalente (ej: "11111111").

    Raises:
        ValueError: Si la cadena no representa un hexadecimal válido.
    """
    raise NotImplementedError("hex-bin pendiente de implementación")
