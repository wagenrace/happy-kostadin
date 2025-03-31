import os
import sys
from pathlib import Path

from tqdm import tqdm

from .get_config.get_config import Config, get_config


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


def main() -> None:
    """Will check all the files for CRLF line endings.
    If the file contains CRLF line endings, it will be replaced with LF line endings.
    If the --fix flag is set, it will fix the line endings.
    If the --fix flag is not set, it will print the files that contain CRLF line endings.
    And, it will raise a sys.exit(1) if any of the files contain CRLF line endings.

    :raises a: sys.exit(1) if any of the files contain CRLF line endings and --fix flag is not set
    :return: None
    """    
    config = get_config()
    print(f"checking for CRLF in {config.path}")

    all_files = get_all_files(config)

    # Usage example
    files_containing_crlf = []
    for file in tqdm(all_files):
        content = open(file, "rb").read()
        if b"\r\n" in content:
            if config.fix:
                content = content.replace(b"\r\n", b"\n")
                with open(file, "wb") as f:
                    f.write(content)
            else:
                file_name = str(file).replace(str(config.path), "")
                files_containing_crlf.append(file_name)

    if files_containing_crlf:
        for file in files_containing_crlf:
            print(f"Error: {file} contains CRLF line ending.")
        print(f"Error: {len(files_containing_crlf)} files contain CRLF line ending.")
        sys.exit(1)
    else:
        print("+=+=+ - You did it tiger! You are free from CRLF - +=+=+")


if __name__ == "__main__":
    main()
