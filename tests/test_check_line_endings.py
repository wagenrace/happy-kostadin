from pathlib import Path
from unittest.mock import patch

import pytest

from src.happy_kostadin.cli import main
from src.happy_kostadin.get_config.get_config import Config


@patch("src.happy_kostadin.cli.get_config")
def test_all_lf(get_config_mock):
    get_config_mock.return_value = Config(
        path=Path(__file__).absolute().parent / Path("test_data_lf"),
        allowed_post_fixes=[],
    )

    try:
        main()
    except SystemExit as excinfo:
        pytest.fail(f"SystemExit was raised with code {excinfo.code}")


@patch("src.happy_kostadin.cli.get_config")
def test_all_crlf(get_config_mock):
    get_config_mock.return_value = Config(
        path=Path(__file__).absolute().parent / Path("test_data_crlf"),
        allowed_post_fixes=[],
    )

    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1


@patch("src.happy_kostadin.cli.get_config")
def test_all_crlf_only_txt(get_config_mock):
    get_config_mock.return_value = Config(
        path=Path(__file__).absolute().parent / Path("test_data_crlf"),
        allowed_post_fixes=["txt"],
    )

    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1


@patch("src.happy_kostadin.cli.get_config")
def test_mix_crlf(get_config_mock):
    get_config_mock.return_value = Config(
        path=Path(__file__).absolute().parent / Path("test_data_mix"),
        allowed_post_fixes=[],
    )

    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1


@patch("src.happy_kostadin.cli.get_config")
def test_mix_crlf_only_tom(get_config_mock):
    get_config_mock.return_value = Config(
        path=Path(__file__).absolute().parent / Path("test_data_mix"),
        allowed_post_fixes=["tom"],
    )

    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1


@patch("src.happy_kostadin.cli.get_config")
def test_mix_crlf_only_tom_and_txt(get_config_mock):
    get_config_mock.return_value = Config(
        path=Path(__file__).absolute().parent / Path("test_data_mix"),
        allowed_post_fixes=["tom", "txt"],
    )

    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1


@patch("src.happy_kostadin.cli.get_config")
def test_mix_crlf_only_txt(get_config_mock):
    get_config_mock.return_value = Config(
        path=Path(__file__).absolute().parent / Path("test_data_mix"),
        allowed_post_fixes=["txt"],
    )

    try:
        main()
    except SystemExit as excinfo:
        pytest.fail(f"SystemExit was raised with code {excinfo.code}")
