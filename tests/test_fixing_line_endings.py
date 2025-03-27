import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from src.happy_kostadin.cli import main
from src.happy_kostadin.get_config.get_config import Config


@patch("src.happy_kostadin.cli.get_config")
def test_fixing_crlf(get_config_mock):
    files_path = Path(__file__).absolute().parent / Path("test_data_crlf")
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)
    for file in (files_path).iterdir():
        if file.is_file():
            target_file = tmp_path / file.name
            target_file.parent.mkdir(parents=True, exist_ok=True)
            target_file.write_bytes(file.read_bytes())

    # Test fails because the test_data_crlf directory contains files with CRLF line endings
    get_config_mock.return_value = Config(
        path=tmp_path,
        allowed_post_fixes=[],
    )

    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1

    # apply fixing
    get_config_mock.return_value = Config(
        path=tmp_path,
        allowed_post_fixes=[],
        fix=True,
    )
    main()

    # Test passes because the test_data_crlf directory contains files with LF line endings
    get_config_mock.return_value = Config(
        path=tmp_path,
        allowed_post_fixes=[],
    )

    try:
        main()
    except SystemExit as excinfo:
        pytest.fail(f"SystemExit was raised with code {excinfo.code}")
