from pathlib import Path

from src.happy_kostadin.cli import get_all_files
from src.happy_kostadin.get_config.get_config import Config


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
        allowed_post_fixes=["txt"],
    )
    all_files = get_all_files(config)
    assert set(all_files) == set(
        [
            Path(__file__).absolute().parent / Path("test_data_lf/file_lf.txt"),
            Path(__file__).absolute().parent / Path("test_data_lf/file_lf2.txt"),
        ]
    )


def test_get_all_files_subfolder():
    config = Config(
        path=Path(__file__).absolute().parent / Path("test_data_mix"),
        allowed_post_fixes=[],
    )
    all_files = get_all_files(config)
    assert set(all_files) == set(
        [
            Path(__file__).absolute().parent / Path("test_data_mix/file_lf.txt"),
            Path(__file__).absolute().parent
            / Path("test_data_mix/sub_folder/file_crlf.tom"),
        ]
    )


def test_get_all_files_subfolder_tom_and_txt():
    config = Config(
        path=Path(__file__).absolute().parent / Path("test_data_mix"),
        allowed_post_fixes=["tom", "txt"],
    )
    all_files = get_all_files(config)
    assert set(all_files) == set(
        [
            Path(__file__).absolute().parent / Path("test_data_mix/file_lf.txt"),
            Path(__file__).absolute().parent
            / Path("test_data_mix/sub_folder/file_crlf.tom"),
        ]
    )


def test_get_all_files_subfolder_only_tom():
    config = Config(
        path=Path(__file__).absolute().parent / Path("test_data_mix"),
        allowed_post_fixes=["tom"],
    )
    all_files = get_all_files(config)
    assert set(all_files) == set(
        [
            Path(__file__).absolute().parent
            / Path("test_data_mix/sub_folder/file_crlf.tom"),
        ]
    )


def test_get_all_files_subfolder_only_txt():
    config = Config(
        path=Path(__file__).absolute().parent / Path("test_data_mix"),
        allowed_post_fixes=["txt"],
    )
    all_files = get_all_files(config)
    assert set(all_files) == set(
        [Path(__file__).absolute().parent / Path("test_data_mix/file_lf.txt")]
    )
