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
    args = get_arguments()
    toml_values = parse_pyproject_toml()
    return Config(
        allowed_post_fixes=toml_values.allowed_post_fixes,
        path=args.path,
        fix=args.fix,
    )
