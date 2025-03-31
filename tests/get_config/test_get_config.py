from pathlib import Path
from unittest import mock

from src.happy_kostadin.get_config.get_args import Args
from src.happy_kostadin.get_config.get_config import Config, get_config
from src.happy_kostadin.get_config.get_toml_values import TomlValues


@mock.patch(
    "src.happy_kostadin.get_config.get_config.get_arguments",
    return_value=Args(path=Path("some/path"), fix=True),
)
@mock.patch(
    "src.happy_kostadin.get_config.get_config.parse_pyproject_toml",
    return_value=TomlValues(allowed_post_fixes=["_test", "_spec"]),
)
def test_get_config(mock_parse_pyproject_toml, mock_get_arguments):
    """Test get_config function with mocked dependencies."""
    result = get_config()
    expected = Config(
        allowed_post_fixes=["_test", "_spec"],
        path=Path("some/path"),
        fix=True,
    )
    assert result == expected
    mock_get_arguments.assert_called_once()
    mock_parse_pyproject_toml.assert_called_once()
