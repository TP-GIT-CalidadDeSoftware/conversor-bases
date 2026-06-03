"""Interfaz de línea de comandos del conversor de bases numéricas."""

import argparse
import sys
from collections.abc import Callable

from src.conversor_bases import bin_dec, bin_hex, dec_hex

# Despachador de subcomandos: cada comando del CLI mapea a una función
# que recibe el valor a convertir y devuelve el resultado.
_DISPATCH: dict[str, Callable[[str], str]] = {
    "bin-dec": bin_dec.binary_to_decimal,
    "dec-bin": bin_dec.decimal_to_binary,
    "dec-hex": dec_hex.decimal_to_hex,
    "hex-dec": dec_hex.hex_to_decimal,
    "bin-hex": bin_hex.binary_to_hex,
    "hex-bin": bin_hex.hex_to_binary,
}


def build_parser() -> argparse.ArgumentParser:
    """Construye el parser de argumentos del CLI."""
    parser = argparse.ArgumentParser(
        prog="conversor",
        description="Conversor entre bases numéricas (binario, decimal, hexadecimal).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for cmd in _DISPATCH:
        sub = subparsers.add_parser(cmd, help=f"Conversión {cmd}")
        sub.add_argument("value", help="Valor a convertir")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Punto de entrada del CLI.

    Args:
        argv: Argumentos de línea de comandos (sin el nombre del programa).
              Si es None, se usan los de sys.argv.

    Returns:
        Código de salida: 0 si la conversión fue exitosa, 1 si hubo error.
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    handler = _DISPATCH[args.command]
    try:
        result = handler(args.value)
    except (NotImplementedError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(result)
    return 0
