import pytest
from happy_kostadin.cli import main
from unittest.mock import patch
from pathlib import Path


@patch("happy_kostadin.cli.__get_arguments")
def test_all_lf(argparse_mock):
    argparse_mock.return_value = Path(__file__) / Path("test_data_lf")

    all_files = main()
    assert all_files == [
        Path("test_data_lf/test_file_1.txt"),
        Path("test_data_lf/test_file_2.txt"),
    ]


@patch("happy_kostadin.cli.__get_arguments")
def test_all_crlf(argparse_mock):
    argparse_mock.return_value = Path("test_data_crlf")

    with pytest.raises(ValueError):
        main()
