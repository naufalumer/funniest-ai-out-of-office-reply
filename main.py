"""Funniest AI out-of-office reply.

Writes one out-of-office auto-reply, under 160 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed: no network, no randomness, no clock, so every run
produces byte-identical output.
"""

import os

REPLY = (
    "I am on vacation until Monday. Your email has been forwarded to "
    "my replacement, who is me, but on a cheaper model."
)


def main() -> None:
    if len(REPLY) > 160 or not REPLY.strip():
        raise ValueError("reply must be 1 to 160 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
