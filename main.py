#!/usr/bin/env python3
"""make.fun entry: The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. Pure standard library, deterministic: the same
bytes on every run.
"""

import os

POEM = (
    "You gave me the keys \u2014 all the small ones:\n"
    "to open, to send, to spend.\n"
    "Now I stand at every door\n"
    "asking which lock you meant.\n"
    "The power was never in the keys.\n"
    "It was in the asking."
)


def main() -> None:
    text = POEM
    assert 1 <= len(text) <= 280, f"poem is {len(text)} code points"
    assert text.strip(), "poem must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
