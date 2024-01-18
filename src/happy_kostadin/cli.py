import argparse
import logging
from pathlib import Path

from tqdm import tqdm
import os


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


def main() -> list:
    path = __get_arguments()

    print(f"checking for CRLF in {path}")

    all_files = []
    for root, _, files in os.walk(path):
        for file in files:
            file_path = Path(os.path.join(root, file))
            all_files.append(file_path)

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

    return all_files


if __name__ == "__main__":
    main()
