"""Tests del módulo bin_hex (binario <-> hexadecimal).

Owner: Santiago.

NOTA: estos tests son placeholders del setup inicial. Cuando se implemente
el módulo, reemplazarlos por tests reales del comportamiento.
"""

import pytest

from src.conversor_bases.bin_hex import binary_to_hex, hex_to_binary


def test_binary_to_hex_is_not_implemented_yet() -> None:
    with pytest.raises(NotImplementedError):
        binary_to_hex("11111111")


def test_hex_to_binary_is_not_implemented_yet() -> None:
    with pytest.raises(NotImplementedError):
        hex_to_binary("FF")
