"""Verify downloaded Halo Office artifacts against the governed manifest."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

EXPECTED = {
    "Halo_Brand_Lift_Intern_Project_Handoff.docx": "74129e1a646acf07b953a0cac4c6c4bdca5bb895db9dc5015e767ba3cfbea35a",
    "Halo_Kickoff_and_Data_Intake.xlsx": "35d0a88ea50bd98b02377a65f5269eb320ce07c7ae1e0428cc8bdf7953a67557",
    "Halo_Project_Starter_Pack.zip": "6f4f73943c5de1cd2d33e8a47523fd42acef96337c58796f30e6a989c87d4e65",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main(folder: Path) -> int:
    failures = 0
    for filename, expected in EXPECTED.items():
        path = folder / filename
        if not path.exists():
            print(f"MISSING  {filename}")
            failures += 1
            continue
        actual = sha256(path)
        if actual == expected:
            print(f"OK       {filename}")
        else:
            print(f"MISMATCH {filename}\n  expected: {expected}\n  actual:   {actual}")
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    raise SystemExit(main(target))
