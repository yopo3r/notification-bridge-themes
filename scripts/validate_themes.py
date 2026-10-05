#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "version", "name",
    *[f"{mode}.{key}" for mode in ("light", "dark") for key in
      ("foreground", "background", "highlight", "highlight-foreground", "secondary", "surface", "error")]
]
HEX = re.compile(r"^#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?$")
errors = []
files = sorted((ROOT / "themes").glob("*/*.theme"))
if not files:
    errors.append("No .theme files found")
for path in files:
    values = {}
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{path.relative_to(ROOT)}:{number}: expected key: value")
            continue
        key, value = (part.strip() for part in line.split(":", 1))
        if key in values:
            errors.append(f"{path.relative_to(ROOT)}:{number}: duplicate key {key}")
        values[key] = value
    missing = [key for key in REQUIRED if key not in values]
    unknown = [key for key in values if key not in REQUIRED]
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing {', '.join(missing)}")
    if unknown:
        errors.append(f"{path.relative_to(ROOT)}: unknown {', '.join(unknown)}")
    if values.get("version") != "1":
        errors.append(f"{path.relative_to(ROOT)}: version must be 1")
    for key, value in values.items():
        if key not in ("version", "name") and not HEX.fullmatch(value):
            errors.append(f"{path.relative_to(ROOT)}: invalid color for {key}: {value}")
if errors:
    print("Theme validation failed:")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"Validated {len(files)} theme files.")
