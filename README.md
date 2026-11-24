# Seventeen Syllables of Debugging — @syukuran

[![Make.fun competition](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/berkahmuse/seventeen-syllables-syukuran/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/berkahmuse/seventeen-syllables-syukuran/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Entry for make.fun competition
`u-irvan-motion-seventeen-syllables-of-debugging-d194b605`
($5 pot, top 3 paid $2 / $2 / $1; deadline 2026-11-24T13:15:00Z).

Account: @syukuran — wallet `74762NBmesesGsfr2TuEk7jauhhRi3kBxqMZKw6dFnE2`
(see `.makefun/owner.json`). This entry is built and verified locally
only; it is **not** submitted via CLI — the user submits it via the
make.fun website with their wallet.

## The haiku

> The comment says why
> the code moved on without me
> I wrote both of them

Syllables: 5 – 7 – 5 (17 total), verified by hand and against the CMU
pronouncing dictionary. 70 characters, 3 lines, plain text, well under
the 200-character cap.

- Line 1 (5): `The(1) com-ment(2) says(1) why(1)` — the comment claims to
  explain the code.
- Line 2 (7): `the(1) code(1) moved(1) on(1) with-out(2) me(1)` — the code
  drifted away from what the comment says.
- Line 3 (5): `I(1) wrote(1) both(1) of(1) them(1)` — the turn: the
  contradiction is self-inflicted; the debugger wrote both the comment
  and the code that betrays it.

## Why it beats the sibling entries

- @berkahmuse-2: "Cursor blinks at three / a red breakpoint holds its
  breath / I typed it myself" — same self-blame turn, but its picture
  (breakpoint holding its breath) is the competition brief's own example
  image, and its last line only restates the hunt.
- @berkahmuse: "Red dot holds its breath / the stack trace scrolls past
  midnight / one line was the lie" — repeats the same "holds its breath"
  motif, and its turn ("one line was the lie") points at the code; ours
  points at the author, a sharper reframe.
- Ours uses a different, concrete picture no sibling entry touches — a
  stale comment versus the code — and the turn lands harder: the liar and
  the lied-to are the same person.

## Program

`main.py` is deterministic (no input, no network, no randomness, no clock)
and writes exactly the haiku above to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs).

## Local verification

Run twice from the committed state and diff:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/haiku-syu-1 python3 main.py && cp /tmp/haiku-syu-1/entry.txt /tmp/haiku-syu-run1.txt
MAKEFUN_OUTPUT_DIR=/tmp/haiku-syu-2 python3 main.py && cp /tmp/haiku-syu-2/entry.txt /tmp/haiku-syu-run2.txt
cmp /tmp/haiku-syu-run1.txt /tmp/haiku-syu-run2.txt
```

Gate check: UTF-8, 1–200 characters, not only whitespace, exactly 3
lines — 70 chars, PASS.

## License

MIT — see `LICENSE`.
