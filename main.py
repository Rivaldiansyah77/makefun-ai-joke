"""make.fun bounty entry: "Make the AI judge laugh" (ai-joke-03).

Writes exactly one deterministic joke to /output/entry.txt
(or $MAKEFUN_OUTPUT for local testing).

Python 3.13, standard library only, no network, no randomness:
the same bytes on every run.
"""

import os

JOKE = "My AI coding agent fixed the bug, then confidently explained why the bug never existed."


def main() -> None:
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
