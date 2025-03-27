import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Args:
    path: Path
    fix: bool = False


def get_arguments() -> Args:
    parser = argparse.ArgumentParser(
        description="A happy Kostadin is a good Kostadin",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "dominant_path",
        type=str,
        help="Get the path to the files you want to check for line endings",
        nargs="?",
        default="",
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        default="",
    )
    parser.add_argument(
        "-f",
        "--fix",
        action='store_true'
    )
    args = parser.parse_args()
    config = vars(args)
    if config.get("dominant_path"):
        path = Path(config["dominant_path"]).absolute()
    elif config.get("path"):
        path = Path(config["path"]).absolute()
    else:
        path = Path.cwd().absolute()

    config = Args(path=path, fix=config.get("fix", False))
    return config
