#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes one original sentence to /output/entry.txt: a modern thing
described to a traveler from 1800 using only words and concepts
that existed before 1800.

The entry describes the experience of a single object — a video
call on a phone — through static sensory metaphors the traveler
already knows: a mirror, a portrait, a voice. No explanation of
how it works, no talk of presses, wires, signals, or any
transmission mechanism; nothing the traveler could not picture
in 1800. The mirror holds the living face of someone three
thousand miles away, and her portrait answers when spoken to —
the thing itself stays guessable from the description alone.
"""

import os
import sys

TEXT = (
    "A small mirror of dark glass holds the living face of your wife, "
    "three thousand miles away, and when you speak, her portrait "
    "answers you at once."
)

MAX_CHARS = 200


def main() -> int:
    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry must be 1-{MAX_CHARS} chars, got {len(text)}",
            file=sys.stderr,
        )
        return 1
    if text.count("\n") != 0:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be blank", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    with open(path, encoding="utf-8") as f:
        read_back = f.read()
    if read_back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
