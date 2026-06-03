"""Tests del CLI router."""

import pytest

from src.conversor_bases.cli import build_parser, main

ALL_COMMANDS = ["bin-dec", "dec-bin", "dec-hex", "hex-dec", "bin-hex", "hex-bin"]


def test_parser_accepts_all_commands() -> None:
    """El parser debe aceptar los 6 subcomandos definidos."""
    parser = build_parser()
    for cmd in ALL_COMMANDS:
        args = parser.parse_args([cmd, "0"])
        assert args.command == cmd
        assert args.value == "0"


def test_parser_requires_command() -> None:
    """Sin subcomando, el parser debe abortar con SystemExit."""
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([])


def test_parser_rejects_unknown_command() -> None:
    """Un subcomando desconocido debe abortar con SystemExit."""
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["foo-bar", "0"])


@pytest.mark.parametrize(
    ("command", "value", "expected"),
    [
        ("dec-hex", "255", "FF"),
        ("hex-dec", "FF", "255"),
    ],
)
def test_main_dec_hex_success(
    command: str, value: str, expected: str, capsys: pytest.CaptureFixture[str]
) -> None:
    """Los comandos dec-hex/hex-dec devuelven 0 e imprimen el resultado."""
    exit_code = main([command, value])
    assert exit_code == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize("command", ["dec-hex", "hex-dec"])
def test_main_dec_hex_invalid_input(command: str, capsys: pytest.CaptureFixture[str]) -> None:
    """Una entrada inválida devuelve 1 y muestra el error por stderr."""
    exit_code = main([command, "ZZ"])
    assert exit_code == 1
    captured = capsys.readouterr()
    assert "Error" in captured.err


@pytest.mark.parametrize(
    ("command", "value", "expected"),
    [
        ("bin-hex", "11111111", "FF"),
        ("hex-bin", "FF", "11111111"),
    ],
)
def test_main_bin_hex_success(
    command: str, value: str, expected: str, capsys: pytest.CaptureFixture[str]
) -> None:
    """Los comandos bin-hex/hex-bin devuelven 0 e imprimen el resultado."""
    exit_code = main([command, value])
    assert exit_code == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize("command", ["bin-hex", "hex-bin"])
def test_main_bin_hex_invalid_input(command: str, capsys: pytest.CaptureFixture[str]) -> None:
    """Una entrada inválida devuelve 1 y muestra el error por stderr."""
    exit_code = main([command, "xyz"])
    assert exit_code == 1
    captured = capsys.readouterr()
    assert "Error" in captured.err


@pytest.mark.parametrize(
    ("command", "value", "expected"),
    [
        ("bin-dec", "1010", "10"),
        ("dec-bin", "10", "1010"),
    ],
)
def test_main_bin_dec_success(
    command: str, value: str, expected: str, capsys: pytest.CaptureFixture[str]
) -> None:
    """Los comandos bin-dec/dec-bin devuelven 0 e imprimen el resultado."""
    exit_code = main([command, value])
    assert exit_code == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize("command", ["bin-dec", "dec-bin"])
def test_main_bin_dec_invalid_input(command: str, capsys: pytest.CaptureFixture[str]) -> None:
    """Una entrada inválida devuelve 1 y muestra el error por stderr."""
    exit_code = main([command, "xyz"])
    assert exit_code == 1
    captured = capsys.readouterr()
    assert "Error" in captured.err
