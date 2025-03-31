import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Args:
    path: Path
    fix: bool = False


def get_arguments() -> Args:
    """Get the arguments from the command line.
    Cleans them up and returns them as a dataclass.

    :return: Args.path (pathlib.Path) - The path to the files you want to check for line endings
    :return: Args.fix (bool) - Whether to fix the line endings or not
    :rtype: Args
    """    
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
    parser.add_argument("-f", "--fix", action="store_true")
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
