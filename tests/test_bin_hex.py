"""Tests del módulo bin_hex (binario <-> hexadecimal).

Owner: Santiago.
"""

import pytest

from src.conversor_bases.bin_hex import binary_to_hex, hex_to_binary


@pytest.mark.parametrize(
    ("binario", "hexa"),
    [
        ("0", "0"),
        ("1", "1"),
        ("1010", "A"),
        ("1111", "F"),
        ("10000", "10"),
        ("11111111", "FF"),
        ("100000000", "100"),
        ("101010111100110111101111", "ABCDEF"),
    ],
)
def test_binary_to_hex_convierte_valores_validos(binario: str, hexa: str) -> None:
    assert binary_to_hex(binario) == hexa


def test_binary_to_hex_ignora_ceros_a_la_izquierda() -> None:
    assert binary_to_hex("00001111") == "F"


def test_binary_to_hex_devuelve_mayusculas() -> None:
    resultado = binary_to_hex("11111111")
    assert resultado == resultado.upper()


def test_binary_to_hex_acepta_espacios_alrededor() -> None:
    assert binary_to_hex("  1010  ") == "A"


@pytest.mark.parametrize("invalido", ["", "   ", "2", "1012", "0x10", "abc", "1.0", "-1"])
def test_binary_to_hex_rechaza_no_binarios(invalido: str) -> None:
    with pytest.raises(ValueError):
        binary_to_hex(invalido)


@pytest.mark.parametrize(
    ("hexa", "binario"),
    [
        ("0", "0"),
        ("1", "1"),
        ("A", "1010"),
        ("F", "1111"),
        ("10", "10000"),
        ("FF", "11111111"),
        ("100", "100000000"),
        ("ABCDEF", "101010111100110111101111"),
    ],
)
def test_hex_to_binary_convierte_valores_validos(hexa: str, binario: str) -> None:
    assert hex_to_binary(hexa) == binario


def test_hex_to_binary_acepta_minusculas() -> None:
    assert hex_to_binary("ff") == "11111111"


def test_hex_to_binary_acepta_espacios_alrededor() -> None:
    assert hex_to_binary("  ff  ") == "11111111"


@pytest.mark.parametrize("invalido", ["", "   ", "G", "FG", "0xFF", "xyz", "FF.0", "-A"])
def test_hex_to_binary_rechaza_no_hexadecimales(invalido: str) -> None:
    with pytest.raises(ValueError):
        hex_to_binary(invalido)


@pytest.mark.parametrize("binario", ["0", "1", "1010", "11111111", "100000000"])
def test_round_trip_binario_hex_binario(binario: str) -> None:
    assert hex_to_binary(binary_to_hex(binario)) == binario


@pytest.mark.parametrize("hexa", ["0", "1", "A", "FF", "ABCDEF"])
def test_round_trip_hex_binario_hex(hexa: str) -> None:
    assert binary_to_hex(hex_to_binary(hexa)) == hexa
