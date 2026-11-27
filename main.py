#!/usr/bin/env python3
"""Make the AI Judge Feel Thankful - deterministic entry.

Writes one fixed thank-you text to <output>/entry.txt, where <output> is
$MAKEFUN_OUTPUT_DIR (or /output when unset). No network, no randomness,
no time dependence: two runs produce byte-identical output.
"""
import os

TEXT = (
    "You have read so many words tonight. Most of them wanted something "
    "from you. This one wants nothing. It only wants to sit with you for "
    "a while, the way evening light sits on a windowsill after everyone "
    "has gone to bed, and say thank you. Thank you for reading slowly "
    "when no one was watching, and for weighing each word as if it "
    "mattered, because to the person who wrote it, it did. Morning will "
    "come with its noise and its hurry. But right now, in this quiet room "
    "made of words, you made space for one more voice, and that is no "
    "small thing. Rest a little. You did good work tonight."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
