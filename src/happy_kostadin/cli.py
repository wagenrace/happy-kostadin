import argparse
import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Dict, Any, Union

from tqdm import tqdm

if sys.version_info >= (3, 11):
    try:
        import tomllib
    except ImportError:
        # Help users on older alphas
        if not TYPE_CHECKING:
            import tomli as tomllib
else:
    import tomli as tomllib


def parse_pyproject_toml() -> Dict[str, Any]:
    """Parse a pyproject toml file, pulling out relevant parts for Black.

    If parsing fails, will raise a tomllib.TOMLDecodeError.
    """
    path_pyproject_toml = Path.cwd() / "pyproject.toml"
    if not path_pyproject_toml.exists():
        return {}
    with open(path_pyproject_toml, "rb") as f:
        pyproject_toml = tomllib.load(f)
    config: Dict[str, Any] = pyproject_toml.get("tool", {}).get("happy_kostadin", {})
    config = {k.replace("--", "").replace("-", "_"): v for k, v in config.items()}

    return config


def __get_arguments() -> Path:
    parser = argparse.ArgumentParser(
        description="A happy Kostadin is a good Kostadin",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Get the path to the files you want to check for line endings",
        default="",
    )
    args = parser.parse_args()
    config = vars(args)
    path = Path(config["path"]).absolute()
    return path


def main(return_checked_files: bool = False) -> Union[list, None]:
    """Will raise a ValueError if any of the files contain CRLF line endings.

    :param return_checked_files: Return all the files tested, defaults to False
    :type return_checked_files: bool, optional
    :raises ValueError: If any of the files contain CRLF line endings
    :return: all the files that are checked or None
    :rtype: Union[list, None]
    """
    path = __get_arguments()
    config = parse_pyproject_toml()
    allowed_post_fixes = tuple(config.get("allowed_post_fixes", []))
    print(f"checking for CRLF in {path}")

    all_files = []
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if len(allowed_post_fixes) > 0:
                if not file_path.endswith(allowed_post_fixes):
                    continue
            all_files.append(Path(file_path))

    # Usage example
    files_containing_crlf = []
    for file in tqdm(all_files):
        content = open(file, "rb").read()
        if b"\r\n" in content:
            files_containing_crlf.append(file)

    if files_containing_crlf:
        raise ValueError(f"{files_containing_crlf} contains CRLF line ending.")
    else:
        print("✨✨ - All files are free from CRLF - ✨✨")

    if return_checked_files:
        return all_files


if __name__ == "__main__":
    main()
