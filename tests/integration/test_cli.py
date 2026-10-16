import subprocess
import sys
from pathlib import Path


def test_cli_help(tmp_path: Path) -> None:
    cli = Path(sys.executable).parent / "authgraph"

    result = subprocess.run(
        [sys.executable, "-I", str(cli), "--help"],
        cwd=tmp_path,
        check=False,
        capture_output=True,
        text=True,
        timeout=10,
    )

    assert result.returncode == 0, result.stderr
    assert "--help" in result.stdout


def test_cli_rejects_unknown_option(tmp_path: Path) -> None:
    cli = Path(sys.executable).parent / "authgraph"

    result = subprocess.run(
        [sys.executable, "-I", str(cli), "--unknown"],
        cwd=tmp_path,
        check=False,
        capture_output=True,
        text=True,
        timeout=10,
    )

    assert result.returncode == 2, result.stderr
    assert "unrecognized arguments" in result.stderr
    assert "--unknown" in result.stderr
