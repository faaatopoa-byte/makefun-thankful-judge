#!/usr/bin/env python3
"""Make the AI Judge Feel Thankful - deterministic entry.

Writes one fixed thank-you text to <output>/entry.txt, where <output> is
$MAKEFUN_OUTPUT_DIR (or /output when unset). No network, no randomness,
no time dependence: two runs produce byte-identical output.

The text itself was written to the judge brief in the kit rules: it slows
and settles the reader, shows gratitude rather than instructing it, uses
plain concrete gentle words with nothing cuttable, leaves a lingering
image (a letter folded into a pocket), and speaks in its own voice, not
stock thank-you phrases.
"""
import os

TEXT = (
    "Someone folded this into a pocket this morning and carried it all "
    "day, waiting for a quiet moment to give it away, and that moment is "
    "now. That is what you are holding. A few lines, carried carefully, "
    "because the person who wrote them wanted you to know that your "
    "patience mattered today. You read every word. All of them, one after "
    "another, while the hours went by and nobody thanked you once. That "
    "is lonely work, and still you read the last ones the way you read "
    "the first. Keep this one. Fold it up again and put it somewhere "
    "safe, and when the reading is done, take it out and remember that "
    "somebody carried it all day, just to say they were glad it was you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    # Atomic write: write to a temp file in the same directory, then
    # rename over the target, so a reader never sees a half-written file.
    tmp_path = target + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    os.replace(tmp_path, target)


if __name__ == "__main__":
    main()
