"""Tests del módulo dec_hex (decimal <-> hexadecimal).

Owner: Augusto Castro.

NOTA: estos tests son placeholders del setup inicial. Cuando se implemente
el módulo, reemplazarlos por tests reales del comportamiento.
"""

import pytest

from src.conversor_bases.dec_hex import decimal_to_hex, hex_to_decimal


def test_decimal_to_hex_is_not_implemented_yet() -> None:
    with pytest.raises(NotImplementedError):
        decimal_to_hex("255")


def test_hex_to_decimal_is_not_implemented_yet() -> None:
    with pytest.raises(NotImplementedError):
        hex_to_decimal("FF")
