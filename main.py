#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
Deterministic, stdlib only, no network access.
"""

import os

LINE = (
    "So... I ran 47 conversation openers through my politeness module "
    "and still landed on 'so'. Nice floor numbers. Very vertical."
)


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-200 chars, single line.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
