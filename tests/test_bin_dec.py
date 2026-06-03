"""Tests del módulo bin_dec (binario <-> decimal).

Owner: Magdalena Rossello.

NOTA: estos tests son placeholders del setup inicial. Cuando se implemente
el módulo, reemplazarlos por tests reales del comportamiento.
"""

import pytest

from src.conversor_bases.bin_dec import binary_to_decimal, decimal_to_binary


def test_binary_to_decimal_is_not_implemented_yet() -> None:
    with pytest.raises(NotImplementedError):
        binary_to_decimal("1010")


def test_decimal_to_binary_is_not_implemented_yet() -> None:
    with pytest.raises(NotImplementedError):
        decimal_to_binary("10")
