import os
import sys
from pathlib import Path
from typing import Union

from tqdm import tqdm

from .get_config.get_config import get_config, Config

def get_all_files(config: Config) -> list:
    all_files = []
    allowed_post_fixes = tuple(config.allowed_post_fixes)
    for root, _, files in os.walk(config.path):
        for file in files:
            file_path = os.path.join(root, file)
            if len(allowed_post_fixes) > 0:
                if not file_path.endswith(allowed_post_fixes):
                    continue
            all_files.append(Path(file_path))
    return all_files

def main(return_checked_files: bool = False) -> Union[list, None]:
    """Will raise a ValueError if any of the files contain CRLF line endings.

    :param return_checked_files: Return all the files tested, defaults to False
    :type return_checked_files: bool, optional
    :raises ValueError: If any of the files contain CRLF line endings
    :return: all the files that are checked or None
    :rtype: Union[list, None]
    """
    config = get_config()
    print(f"checking for CRLF in {config.path}")

    all_files = get_all_files(config)

    # Usage example
    files_containing_crlf = []
    for file in tqdm(all_files):
        content = open(file, "rb").read()
        if b"\r\n" in content:
            file_name = str(file).replace(str(config.path), "")
            files_containing_crlf.append(file_name)

    if files_containing_crlf:
        for file in files_containing_crlf:
            print(f"Error: {file} contains CRLF line ending.")
        print(f"Error: {len(files_containing_crlf)} files contain CRLF line ending.")
        sys.exit(1)
    else:
        print("+=+=+ - All files are free from CRLF - +=+=+")

    if return_checked_files:
        return all_files


if __name__ == "__main__":
    main()
