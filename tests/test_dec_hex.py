"""Tests del módulo dec_hex (decimal <-> hexadecimal).

Owner: Augusto Castro.
"""

import pytest

from src.conversor_bases.dec_hex import decimal_to_hex, hex_to_decimal


def test_decimal_to_hex_basico() -> None:
    assert decimal_to_hex("255") == "FF"
    assert decimal_to_hex("16") == "10"
    assert decimal_to_hex("0") == "0"


def test_hex_to_decimal_basico() -> None:
    assert hex_to_decimal("FF") == "255"
    assert hex_to_decimal("10") == "16"
    assert hex_to_decimal("0") == "0"


def test_hex_to_decimal_acepta_minusculas() -> None:
    assert hex_to_decimal("ff") == "255"
    assert hex_to_decimal("aB") == "171"


def test_ida_y_vuelta() -> None:
    for decimal in ("0", "15", "255", "4096"):
        assert hex_to_decimal(decimal_to_hex(decimal)) == decimal


def test_decimal_to_hex_invalido() -> None:
    for invalido in ("", "12.5", "-3", "FF", " 10", "abc"):
        with pytest.raises(ValueError):
            decimal_to_hex(invalido)


def test_hex_to_decimal_invalido() -> None:
    for invalido in ("", "GG", "12Z", " FF", "0x1A"):
        with pytest.raises(ValueError):
            hex_to_decimal(invalido)
