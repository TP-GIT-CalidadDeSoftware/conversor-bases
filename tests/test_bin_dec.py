"""Tests del módulo bin_dec (binario <-> decimal).

Owner: Magdalena Rossello.
"""

import pytest

from src.conversor_bases.bin_dec import binary_to_decimal, decimal_to_binary


@pytest.mark.parametrize(
    ("binario", "decimal"),
    [
        ("0", "0"),
        ("1", "1"),
        ("10", "2"),
        ("1010", "10"),
        ("1111", "15"),
        ("10000", "16"),
        ("11111111", "255"),
        ("100000000", "256"),
        ("1111111111", "1023"),
    ],
)
def test_binary_to_decimal_convierte_valores_validos(binario: str, decimal: str) -> None:
    assert binary_to_decimal(binario) == decimal


def test_binary_to_decimal_ignora_ceros_a_la_izquierda() -> None:
    assert binary_to_decimal("00001010") == "10"


def test_binary_to_decimal_acepta_espacios_alrededor() -> None:
    assert binary_to_decimal("  1010  ") == "10"


@pytest.mark.parametrize("invalido", ["", "   ", "2", "1012", "0b10", "abc", "1.0", "-1"])
def test_binary_to_decimal_rechaza_no_binarios(invalido: str) -> None:
    with pytest.raises(ValueError):
        binary_to_decimal(invalido)


@pytest.mark.parametrize(
    ("decimal", "binario"),
    [
        ("0", "0"),
        ("1", "1"),
        ("2", "10"),
        ("10", "1010"),
        ("15", "1111"),
        ("16", "10000"),
        ("255", "11111111"),
        ("256", "100000000"),
        ("1023", "1111111111"),
    ],
)
def test_decimal_to_binary_convierte_valores_validos(decimal: str, binario: str) -> None:
    assert decimal_to_binary(decimal) == binario


def test_decimal_to_binary_acepta_espacios_alrededor() -> None:
    assert decimal_to_binary("  10  ") == "1010"


@pytest.mark.parametrize("invalido", ["", "   ", "abc", "10.5", "-3", "0x10", "1e10"])
def test_decimal_to_binary_rechaza_no_decimales(invalido: str) -> None:
    with pytest.raises(ValueError):
        decimal_to_binary(invalido)


@pytest.mark.parametrize("binario", ["0", "1", "10", "1010", "11111111", "100000000"])
def test_round_trip_binario_decimal_binario(binario: str) -> None:
    assert decimal_to_binary(binary_to_decimal(binario)) == binario


@pytest.mark.parametrize("decimal", ["0", "1", "10", "255", "1023"])
def test_round_trip_decimal_binario_decimal(decimal: str) -> None:
    assert binary_to_decimal(decimal_to_binary(decimal)) == decimal
