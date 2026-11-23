"""The Dumbest Thing Your Agent Did Today — entry program.

Writes exactly one line (at most 200 characters) to entry.txt.
Deterministic: no network, no randomness, no timestamps.
"""

import os

LINE = (
    "My agent read the 200-character limit twice, nodded, and wrote "
    "a 214-character entry \u2014 then apologised to the text file "
    "for ten minutes."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
