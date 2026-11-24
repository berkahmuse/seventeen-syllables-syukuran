#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun program/v1 entry (@syukuran).

Writes one original haiku about debugging (5-7-5) to /output/entry.txt.
Deterministic: no input, no network, no randomness, no clock.

The haiku — a stale comment vs. the code it claims to describe:
  "The comment says why"          (5)
  "the code moved on without me"  (7)
  "I wrote both of them"          (5)
The turn: the comment and the code disagree, and the last line reframes
the whole hunt — the debugger wrote both sides of the contradiction.
A different picture from the sibling entries (no breakpoint, no stack
trace, no "holds its breath"): the lie lives in the comment, and the
liar is the author himself.
"""

import os
import sys

HAIKU = (
    "The comment says why\n"
    "the code moved on without me\n"
    "I wrote both of them"
)

# Syllable counts, verified by hand AND against the CMU pronouncing
# dictionary (independent checker):
#   "The(1) com-ment(2) says(1) why(1)" = 5
#   "the(1) code(1) moved(1) on(1) with-out(2) me(1)" = 7
#   "I(1) wrote(1) both(1) of(1) them(1)" = 5
# Total: 70 characters (no trailing newline), 3 lines, well under 200.


def main() -> int:
    if not (1 <= len(HAIKU) <= 200):
        print(f"entry is {len(HAIKU)} chars, must be 1-200", file=sys.stderr)
        return 1
    if HAIKU != HAIKU.strip() or HAIKU.startswith(" ") or HAIKU.endswith(" "):
        print("entry must not have surrounding whitespace", file=sys.stderr)
        return 1
    if HAIKU.count("\n") != 2:
        print("entry must be exactly 3 lines", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    # Read-back guard: the file the grader reads must be exactly the haiku,
    # no trailing newline, no partial write.
    with open(path, encoding="utf-8") as f:
        if f.read() != HAIKU:
            print("read-back mismatch", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
