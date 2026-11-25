#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message -- the note an AI agent would leave in the
log after a long night of chasing down and fixing its own bugs -- to
/output/entry.txt. One line, at most 200 characters.
"""

import os

LINE = (
    "fix: nine hours. The bug was a comment I wrote at midnight saying "
    "'this cannot fail'. I deleted the comment. "
    "The code, at last, cannot fail."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
