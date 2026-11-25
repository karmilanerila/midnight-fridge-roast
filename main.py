"""Midnight Fridge Roast — one-line roast for a smart fridge.

The program writes a single roast line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when the grader sets it).
Standard library only; no network, no temp files.
"""

import os

# Angle: the fridge as a nightclub bouncer. The joke lands on the
# midnight rule itself — the owner who stocked the fridge is
# suddenly not on the list — not on the appliance in general.
LINE = (
    "After midnight, my fridge turns bouncer: checks my ID, "
    "shakes its head, and tells the man who bought the snacks "
    "he's not on the list."
)


def main() -> None:
    # The gate accepts 1-200 UTF-8 characters; refuse to emit
    # anything outside that window rather than ship a bad line.
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("roast line must be a single line")
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"roast line is {len(LINE)} chars, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
