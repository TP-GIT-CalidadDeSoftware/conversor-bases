"""Conversión entre binario y decimal."""


def binary_to_decimal(value: str) -> str:
    """Convierte un número binario (cadena) a decimal (cadena).

    Args:
        value: Cadena con el número binario (ej: "1010").

    Returns:
        Cadena con el número decimal equivalente (ej: "10").

    Raises:
        ValueError: Si la cadena no representa un binario válido.
    """
    normalized = value.strip()
    if not normalized or any(ch not in "01" for ch in normalized):
        raise ValueError(f"'{value}' no es un binario válido")
    return str(int(normalized, 2))


def decimal_to_binary(value: str) -> str:
    """Convierte un número decimal (cadena) a binario (cadena).

    Args:
        value: Cadena con el número decimal (ej: "10").

    Returns:
        Cadena con el número binario equivalente (ej: "1010").

    Raises:
        ValueError: Si la cadena no representa un decimal válido.
    """
    normalized = value.strip()
    if not normalized or not normalized.isdigit():
        raise ValueError(f"'{value}' no es un decimal válido")
    return format(int(normalized), "b")
