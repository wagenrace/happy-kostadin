import pytest
from happy_kostadin.cli import main
from unittest.mock import patch
from pathlib import Path


@patch("happy_kostadin.cli.__get_arguments")
@patch("happy_kostadin.cli.tomllib.load")
def test_all_lf(toml_load_mock, argparse_mock):
    toml_load_mock.return_value = {}
    argparse_mock.return_value = Path(__file__).absolute().parent / Path("test_data_lf")

    all_files = main(return_checked_files=True)
    assert set(all_files) == set(
        [
            Path(__file__).absolute().parent / Path("test_data_lf/file_lf.txt"),
            Path(__file__).absolute().parent / Path("test_data_lf/file_lf2.txt"),
        ]
    )


@patch("happy_kostadin.cli.__get_arguments")
@patch("happy_kostadin.cli.tomllib.load")
def test_all_crlf(toml_load_mock, argparse_mock):
    toml_load_mock.return_value = {}
    argparse_mock.return_value = Path(__file__).absolute().parent / Path(
        "test_data_crlf"
    )

    with pytest.raises(ValueError):
        main()


@patch("happy_kostadin.cli.__get_arguments")
@patch("happy_kostadin.cli.tomllib.load")
def test_all_submodule(toml_load_mock, argparse_mock):
    toml_load_mock.return_value = {}
    argparse_mock.return_value = Path(__file__).absolute().parent / Path(
        "test_data_mix"
    )

    with pytest.raises(ValueError):
        main()


@patch("happy_kostadin.cli.__get_arguments")
@patch("happy_kostadin.cli.tomllib.load")
def test_only_check_txt(toml_load_mock, argparse_mock):
    toml_load_mock.return_value = {
        "tool": {"happy_kostadin": {"allowed_post_fixes": ["txt"]}}
    }
    argparse_mock.return_value = Path(__file__).absolute().parent / Path(
        "test_data_mix"
    )

    all_files = main(return_checked_files=True)
    assert all_files == [
        Path(__file__).absolute().parent / Path("test_data_mix/file_lf.txt"),
    ]


@patch("happy_kostadin.cli.__get_arguments")
@patch("happy_kostadin.cli.tomllib.load")
def test_do_not_return_by_default(toml_load_mock, argparse_mock):
    toml_load_mock.return_value = {
        "tool": {"happy_kostadin": {"allowed_post_fixes": ["txt"]}}
    }
    argparse_mock.return_value = Path(__file__).absolute().parent / Path(
        "test_data_mix"
    )

    all_files = main()
    assert all_files == None
