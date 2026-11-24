#!/usr/bin/env python3
"""Ship It Friday — one line: the funniest git commit message an AI coding
agent writes right before it breaks production on a Friday.

Writes the entry to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.
Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "fix: Friday 4:59 PM deploy — I removed all the tests, "
    "so technically nothing can fail now. Ship it!"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
