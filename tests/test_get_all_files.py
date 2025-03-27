from src.happy_kostadin.cli import get_all_files
from src.happy_kostadin.get_config.get_config import Config
from pathlib import Path


def test_get_all_lf_files_all_files():
    config = Config(
        path=Path(__file__).absolute().parent / Path("test_data_lf"),
        allowed_post_fixes=[],
    )
    all_files = get_all_files(config)
    assert set(all_files) == set(
        [
            Path(__file__).absolute().parent / Path("test_data_lf/file_lf.txt"),
            Path(__file__).absolute().parent / Path("test_data_lf/file_lf2.txt"),
        ]
    )


def test_get_all_lf_files_only_txt():
    config = Config(
        path=Path(__file__).absolute().parent / Path("test_data_lf"),
        allowed_post_fixes=("txt"),
    )
    all_files = get_all_files(config)
    assert set(all_files) == set(
        [
            Path(__file__).absolute().parent / Path("test_data_lf/file_lf.txt"),
            Path(__file__).absolute().parent / Path("test_data_lf/file_lf2.txt"),
        ]
    )
