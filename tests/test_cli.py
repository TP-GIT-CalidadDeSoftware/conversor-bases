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


@pytest.mark.parametrize("command", ALL_COMMANDS)
def test_main_returns_error_when_not_implemented(
    command: str, capsys: pytest.CaptureFixture[str]
) -> None:
    """Mientras los módulos no estén implementados, main devuelve 1 y muestra error."""
    exit_code = main([command, "0"])
    assert exit_code == 1
    captured = capsys.readouterr()
    assert "Error" in captured.err
