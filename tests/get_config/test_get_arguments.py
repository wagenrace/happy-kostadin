from pathlib import Path
from unittest import mock

from src.happy_kostadin.get_config.get_args import Args, get_arguments


@mock.patch("sys.argv", ["program_name"])
def test_default_arguments():
    result = get_arguments()
    expected = Args(path=Path.cwd().absolute(), fix=False)
    assert result == expected


@mock.patch("sys.argv", ["program_name", "some/path"])
def test_dominant_path_argument():
    result = get_arguments()
    expected = Args(path=Path("some/path").absolute(), fix=False)
    assert result == expected


@mock.patch("sys.argv", ["program_name", "-p", "another/path"])
def test_path_argument():
    result = get_arguments()
    expected = Args(path=Path("another/path").absolute(), fix=False)
    assert result == expected


@mock.patch("sys.argv", ["program_name", "-f", "True"])
def test_fix_argument():
    result = get_arguments()
    expected = Args(path=Path.cwd().absolute(), fix=True)
    assert result == expected


@mock.patch("sys.argv", ["program_name", "some/path", "-f", "True"])
def test_dominant_path_and_fix_arguments():
    result = get_arguments()
    expected = Args(path=Path("some/path").absolute(), fix=True)
    assert result == expected


@mock.patch("sys.argv", ["program_name", "-p", "another/path", "-f", "True"])
def test_path_and_fix_arguments():
    result = get_arguments()
    expected = Args(path=Path("another/path").absolute(), fix=True)
    assert result == expected


@mock.patch(
    "sys.argv",
    [
        "program_name",
        "some/path",
        "-p",
        "another/path",
    ],
)
def test_dominant_path_over_path():
    result = get_arguments()
    expected = Args(path=Path("some/path").absolute(), fix=False)
    assert result == expected
