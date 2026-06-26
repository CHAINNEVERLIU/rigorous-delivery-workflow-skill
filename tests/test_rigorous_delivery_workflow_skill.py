import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCANNER = ROOT / "skills" / "rigorous-delivery-workflow" / "scripts" / "scan-red-flags.py"


def run_scanner(*paths: Path | str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCANNER), *(str(path) for path in paths)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def test_scan_red_flags_passes_clean_artifact(tmp_path: Path) -> None:
    artifact = tmp_path / "clean.md"
    artifact.write_text("Requirement: verify behavior with a concrete command.\n", encoding="utf-8")

    result = run_scanner(artifact)

    assert result.returncode == 0
    assert "[OK]" in result.stdout


def test_scan_red_flags_flags_lowercase_and_chinese_vague_terms(tmp_path: Path) -> None:
    artifact = tmp_path / "bad.md"
    vague_chinese = "\u8fd9\u91cc\u5148\u9002\u5f53\u5904\u7406\uff0c\u540e\u7eed\u518d\u8bf4\u3002"
    artifact.write_text(
        f"todo: revisit the acceptance evidence.\n{vague_chinese}\n",
        encoding="utf-8",
    )

    result = run_scanner(artifact)

    assert result.returncode == 1
    assert "[FAIL] Red flags found:" in result.stdout
    assert "todo: revisit the acceptance evidence." in result.stdout
    assert "\u9002\u5f53\u5904\u7406" in result.stdout


def test_scan_red_flags_fails_for_missing_path(tmp_path: Path) -> None:
    result = run_scanner(tmp_path / "missing.md")

    assert result.returncode != 0
    assert "[FAIL] Missing path" in result.stderr


def test_scan_red_flags_does_not_allow_artifact_inline_bypass(tmp_path: Path) -> None:
    artifact = tmp_path / "bad.md"
    artifact.write_text("TODO: missing evidence.  # red-flag-allow\n", encoding="utf-8")

    result = run_scanner(artifact)

    assert result.returncode == 1
    assert "TODO: missing evidence." in result.stdout
