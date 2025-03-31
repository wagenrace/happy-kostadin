from dataclasses import dataclass
from pathlib import Path
from typing import List

from .get_args import get_arguments
from .get_toml_values import parse_pyproject_toml


@dataclass
class Config:
    allowed_post_fixes: List[str]
    path: Path
    fix: bool = False


def get_config() -> Config:
    """Get the config for the script.
    This will get the config from the command line and the pyproject.toml file.

    :return: Config.allowed_post_fixes (list[str]) - The allowed post fixes
    :return: Config.path (pathlib.Path) - The path to the files you want to check for line endings
    :return: Config.fix (bool) - Whether to fix the line endings or not
    :rtype: Config
    """    
    args = get_arguments()
    toml_values = parse_pyproject_toml()
    return Config(
        allowed_post_fixes=toml_values.allowed_post_fixes,
        path=args.path,
        fix=args.fix,
    )
