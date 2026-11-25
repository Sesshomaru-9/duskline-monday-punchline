#!/usr/bin/env python3
"""Duskline Monday Punchline.

Entry for make.fun bounty u-gentle-badger-68-monday-morning-punchlines-709645dc
("Monday Morning Punchlines"): one joke about Monday mornings, written to
``$MAKEFUN_OUTPUT_DIR/entry.txt``.

The program is deterministic, standard library only, and never touches the
network. It writes exactly one file, ``entry.txt``, and only inside the
output directory it is given. If that directory is the repository itself
(or lives inside it) the program refuses quietly: it exits 0 having written
nothing. Nothing here ever raises to the caller: any failure exits 0
having written nothing.
"""

import os
import sys
import tempfile

# The joke, written with escapes so the special characters are unambiguous:
# \u2019 is the curly apostrophe in "I\u2019d" and "it\u2019s", \u2018 / \u2019 are
# the single quotes around Monday's reply, \u2014 is the em-dash.
SETUP = "I told Monday I\u2019d call in sick."
PUNCHLINE = "Monday said, \u2018You already did \u2014 it\u2019s called the weekend.\u2019"

LINE = SETUP + " " + PUNCHLINE

# Why this line: the setup hands Monday a voice, and the punchline lets
# Monday answer back — the weekend was the sick day all along, already
# taken. No alarm, no coffee, no traffic: the complaint is the joke's
# straight man, not the joke.

HERE = os.path.dirname(os.path.abspath(__file__))


def _is_in_repo(directory):
    """True when *directory* is the repo dir or lives inside it."""
    try:
        target = os.path.realpath(directory)
        root = os.path.realpath(HERE)
    except Exception:
        return True
    return target == root or target.startswith(root + os.sep)


def _looks_valid(line):
    """Gate check: one non-blank line, 1-200 chars, encodable as UTF-8."""
    if not line or line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    if not 1 <= len(line) <= 200:
        return False
    try:
        line.encode("utf-8")
    except Exception:
        return False
    return True


def _resolve_output_dir():
    """Pick the output directory, or None when there is nowhere safe."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    if not out:
        try:
            out = tempfile.mkdtemp(prefix="duskline-monday-punchline-")
        except Exception:
            return None
    if _is_in_repo(out):
        return None
    return out


def _write_entry(path, line):
    """Write *line* to *path* with no trailing newline, then verify it."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, "r", encoding="utf-8") as handle:
        if handle.read() != line:
            raise ValueError("round-trip mismatch")


def run():
    if not _looks_valid(LINE):
        return 0

    out = _resolve_output_dir()
    if out is None:
        return 0

    try:
        os.makedirs(out, exist_ok=True)
    except Exception:
        return 0

    path = os.path.join(out, "entry.txt")
    if _is_in_repo(path):
        return 0

    try:
        _write_entry(path, LINE)
    except Exception:
        try:
            os.remove(path)
        except Exception:
            pass
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(run())
