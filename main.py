#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes one original roast of my own AI agent, a single line of at most
200 characters, to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

Standard library only. No network access. Deterministic: the same line is
written on every run.
"""

import os
import sys

LINE = "I asked my agent to keep it short. It replied with a plan, a checklist, and a 12-slide deck about brevity."


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Verify the write round-trips: what the grader reads must be exactly
    # the validated line, not a partial or re-encoded write.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != LINE + "\n":
            print("written entry does not round-trip", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
