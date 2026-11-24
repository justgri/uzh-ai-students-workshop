#!/usr/bin/env python3
"""Copy the three selected final presentation PDFs to website downloads."""

import argparse
import filecmp
from pathlib import Path
import shutil
import sys


PDF_NAMES = (
    "intro_agentic_ai.pdf",
    "intro_agentic_ai_blue.pdf",
    "intro_agentic_ai_blue_columns.pdf",
)


def sync_pdfs(repository: Path, *, check: bool = False) -> int:
    """Check or copy exactly the selected PDF names within a repository."""
    source_dir = repository / "presentation" / "final"
    destination_dir = repository / "site" / "downloads"
    missing_sources = [name for name in PDF_NAMES if not (source_dir / name).is_file()]
    if missing_sources:
        for name in missing_sources:
            print(f"Missing source: {source_dir / name}", file=sys.stderr)
        return 1

    if not check:
        destination_dir.mkdir(parents=True, exist_ok=True)
        for name in PDF_NAMES:
            shutil.copyfile(source_dir / name, destination_dir / name)

    failures = []
    for name in PDF_NAMES:
        destination = destination_dir / name
        if not destination.is_file():
            failures.append(f"Missing website PDF: {destination}")
        elif not filecmp.cmp(source_dir / name, destination, shallow=False):
            failures.append(f"Different PDF bytes: {destination}")

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    action = "Checked" if check else "Copied and verified"
    print(f"{action} all three presentation PDFs.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="check missing files and byte equality without writing"
    )
    args = parser.parse_args()
    repository = Path(__file__).resolve().parents[1]
    try:
        return sync_pdfs(repository, check=args.check)
    except OSError as error:
        print(f"Presentation PDF sync failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
