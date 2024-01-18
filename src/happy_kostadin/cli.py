import argparse
from pathlib import Path


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
    path = config["path"]
    return path


def main():
    path = __get_arguments()

    print(path)


if __name__ == "__main__":
    main()
