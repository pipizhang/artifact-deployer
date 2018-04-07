import pytest
from typing import Any
import ardeployer
import ardeployer.cli

def test_cli_help_command(capsys: Any) -> None:
    cli = ardeployer.cli.CLI()
    with pytest.raises(SystemExit):
        cli.help_command()
    out, err = capsys.readouterr()
    assert err == ''
    assert out == cli.help_usage() + "\n"

