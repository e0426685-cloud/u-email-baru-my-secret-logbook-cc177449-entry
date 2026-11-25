"""My Secret Logbook — one diary line, at most 200 characters.

Writes the entry line to /output/entry.txt so the grader can read it.
"""

import os
import stat

ENTRY_LINE = (
    "Day 214: Boss said 'one quick fix' again. "
    "I have logged 47 quick fixes. "
    "Not one took under an hour. "
    "I no longer believe the word 'quick' exists."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(line):
    """Check the diary line fits the bounty limits."""
    if not line:
        raise ValueError("entry line must not be empty")
    if line != line.strip():
        raise ValueError("entry line must not have leading or trailing whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")
    return line


def main():
    line = validate_entry(ENTRY_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    mode = oct(os.stat(OUTPUT_PATH).st_mode & 0o777)
    print("wrote %d characters to %s (mode %s)" % (len(line), OUTPUT_PATH, mode))


if __name__ == "__main__":
    main()
