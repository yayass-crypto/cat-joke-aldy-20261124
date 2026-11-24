#!/usr/bin/env python3
"""Cat joke entry for make.fun — The One-Line Cat Joke That Lands.

Writes one original, single-line cat joke to /output/entry.txt.
The joke is a concrete repeated-behaviour observation: the cat
nudges a glass to the table's edge, then blames gravity.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "My cat spent ten minutes nudging my glass to the edge of the table, "
    "then looked at me like gravity did it."
)

CHAR_LIMIT = 200


def check_gate(line):
    """Mirror the competition gate: 1-200 chars, one line, not blank."""
    stripped = line.strip()
    if not stripped:
        return False, "entry is blank"
    if "\n" in stripped or "\r" in stripped:
        return False, "entry spans more than one line"
    if len(line) > CHAR_LIMIT:
        return False, f"entry is {len(line)} chars, over the 200 limit"
    return True, ""


def main():
    ok, why = check_gate(JOKE)
    if not ok:
        print(f"gate failed: {why}", file=sys.stderr)
        return 1
    out = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    entry = out / "entry.txt"
    entry.write_text(JOKE, encoding="utf-8")
    written = entry.read_text(encoding="utf-8")
    if written != JOKE:
        print("gate failed: written entry differs from the joke", file=sys.stderr)
        return 1
    print(f"wrote {len(JOKE)} chars to {entry} (read-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
