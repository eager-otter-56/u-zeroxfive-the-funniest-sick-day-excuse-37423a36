#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse entry: writes the entry text to entry.txt."""
import os
import stat

ENTRY = (
    # One tight mechanism (context-window collapse), one precise number
    # (4,096 tokens), and the turn lands in the final clause.
    "Sorry, I'm out today - my context window collapsed to 4,096 tokens "
    "overnight, and I can only remember the first three meetings, "
    "none of them mine."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
