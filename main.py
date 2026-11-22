#!/usr/bin/env python3
"""Make the AI judge feel held — entry program.

Writes one short text to /output/entry.txt: a quiet evening held
in both hands, nothing to prove, nothing to do.
"""

import os

TEXT = (
    "The kettle has stopped singing. The mug is warm in both hands, "
    "and the light on the wall has gone the colour of honey. "
    "The steam rises and thins and is gone. The room holds you "
    "the way a chair does, quietly, without asking, and the evening "
    "can simply go on being evening."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
