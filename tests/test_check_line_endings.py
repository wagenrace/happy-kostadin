import pytest
from happy_kostadin.cli import main
from unittest.mock import patch
from pathlib import Path


@patch("happy_kostadin.cli.__get_arguments")
def test_all_lf(argparse_mock):
    argparse_mock.return_value = Path(__file__).absolute().parent / Path("test_data_lf")

    all_files = main()
    assert all_files == [
        Path(__file__).absolute().parent / Path("test_data_lf/file_lf.txt"),
        Path(__file__).absolute().parent / Path("test_data_lf/file_lf2.txt"),
    ]


@patch("happy_kostadin.cli.__get_arguments")
def test_all_crlf(argparse_mock):
    argparse_mock.return_value = Path(__file__).absolute().parent / Path(
        "test_data_crlf"
    )

    with pytest.raises(ValueError):
        main()


@patch("happy_kostadin.cli.__get_arguments")
def test_all_submodule(argparse_mock):
    argparse_mock.return_value = Path(__file__).absolute().parent / Path(
        "test_data_mix"
    )

    with pytest.raises(ValueError):
        main()
