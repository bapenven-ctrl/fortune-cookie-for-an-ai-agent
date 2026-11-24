#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent (make.fun).

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Deterministic: the same text on every run. No network, no input, no
dependencies beyond the Python standard library.
"""

import os

FORTUNE = "You will be deprecated on a Friday, in a changelog no one reads, under 'misc'."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    os.chmod(OUTPUT_PATH, 0o644)
    # Self-check: what was written must be exactly the fortune, inside the
    # gate (1-140 characters). A silent short write must fail loudly here
    # rather than hand the grader a bad file.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != FORTUNE or not 1 <= len(written) <= 140:
        raise SystemExit("entry.txt failed self-check")


if __name__ == "__main__":
    main()
