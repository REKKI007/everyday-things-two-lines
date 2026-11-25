#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run -- make.fun entry.

Writes the chosen two-line explanation to /output/entry.txt.
Standard library only. Deterministic: the same bytes on every run.
No network, no environment secrets, nothing read from outside this file.

Line 1 explains a toaster to a 10-year-old in a single vivid sentence
built on one concrete, surprising analogy (a pinball machine). Line 2
says in one sentence what the analogy maps and what it leaves out.
"""

import os

ENTRY = (
    "A toaster is a tiny pinball machine for bread that browns your slice "
    "with hidden hot wires and then shoots it up with a spring when the timer "
    "runs out.\n"
    "The pinball machine covers the waiting, the ding, and the pop-up "
    "launch, but it leaves out the real heat, the crumbs at the bottom, "
    "and the fact that there is no ball and no score to beat."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Gate self-check (mirrors the sealed scorer): UTF-8 text of
    # 1-400 characters, not only whitespace, exactly two lines.
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert len(ENTRY.splitlines()) == 2, "entry must be exactly two lines"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    # The grader collects outputs as another user: leave the file
    # (and the folder) readable by everyone.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
