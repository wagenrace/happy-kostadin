import tomllib
from unittest import mock

import pytest

from src.happy_kostadin.get_config.get_toml_values import (
    TomlValues,
    parse_pyproject_toml,
)


@pytest.fixture
def mock_pyproject_toml(tmp_path):
    """Fixture to create a temporary pyproject.toml file."""
    pyproject_path = tmp_path / "pyproject.toml"
    yield pyproject_path
    if pyproject_path.exists():
        pyproject_path.unlink()


def test_parse_pyproject_toml_no_file(mock_pyproject_toml):
    """Test when pyproject.toml does not exist."""
    with mock.patch("pathlib.Path.cwd", return_value=mock_pyproject_toml.parent):
        result = parse_pyproject_toml()
        expected = TomlValues(allowed_post_fixes=[])
        assert result == expected


def test_parse_pyproject_toml_empty_file(mock_pyproject_toml):
    """Test when pyproject.toml exists but is empty."""
    mock_pyproject_toml.write_text("")
    with mock.patch("pathlib.Path.cwd", return_value=mock_pyproject_toml.parent):
        result = parse_pyproject_toml()
        expected = TomlValues(allowed_post_fixes=[])
        assert result == expected


def test_parse_pyproject_toml_valid_config(mock_pyproject_toml):
    """Test when pyproject.toml contains valid configuration."""
    mock_pyproject_toml.write_text(
        """
        [tool.happy_kostadin]
        allowed_post_fixes = ["_test", "_spec"]
        """
    )
    with mock.patch("pathlib.Path.cwd", return_value=mock_pyproject_toml.parent):
        result = parse_pyproject_toml()
        expected = TomlValues(allowed_post_fixes=["_test", "_spec"])
        assert result == expected


def test_parse_pyproject_toml_missing_section(mock_pyproject_toml):
    """Test when pyproject.toml does not contain the relevant section."""
    mock_pyproject_toml.write_text(
        """
        [tool.other_tool]
        some_key = "some_value"
        """
    )
    with mock.patch("pathlib.Path.cwd", return_value=mock_pyproject_toml.parent):
        result = parse_pyproject_toml()
        expected = TomlValues(allowed_post_fixes=[])
        assert result == expected


def test_parse_pyproject_toml_invalid_toml(mock_pyproject_toml):
    """Test when pyproject.toml contains invalid TOML syntax."""
    mock_pyproject_toml.write_text(
        """
        [tool.happy_kostadin
        allowed_post_fixes = ["_test", "_spec"]
        """
    )
    with mock.patch("pathlib.Path.cwd", return_value=mock_pyproject_toml.parent):
        with pytest.raises(tomllib.TOMLDecodeError):
            parse_pyproject_toml()
