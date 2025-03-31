import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, List

# This needs to stay here till Python 3.10 is deprecated (October 2026)
# https://peps.python.org/pep-0619/
if sys.version_info >= (3, 11):
    try:
        import tomllib
    except ImportError:
        # Help users on older alphas
        if not TYPE_CHECKING:
            import tomli as tomllib
else:
    import tomli as tomllib


@dataclass
class TomlValues:
    allowed_post_fixes: List[str]


def parse_pyproject_toml() -> TomlValues:
    """Get the parameters from the pyproject.toml file.
    This will return the parameters as a dataclass.
    If the file does not exist, it will return an empty dataclass.

    :raises a: tomllib.TOMLDecodeError if parsing fails
    :return: TomlValues.allowed_post_fixes (list[str]) - The allowed post fixes
    :rtype: TomlValues
    """
    path_pyproject_toml = Path.cwd() / "pyproject.toml"
    if not path_pyproject_toml.exists():
        return TomlValues(allowed_post_fixes=[])
    with open(path_pyproject_toml, "rb") as f:
        pyproject_toml = tomllib.load(f)
    raw_config: Dict[str, Any] = pyproject_toml.get("tool", {}).get(
        "happy_kostadin", {}
    )
    raw_config = {
        k.replace("--", "").replace("-", "_"): v for k, v in raw_config.items()
    }

    config = TomlValues(allowed_post_fixes=raw_config.get("allowed_post_fixes", []))
    return config
