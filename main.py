"""One Line, One Laugh — make.fun entry.

Writes a single funny line to /output/entry.txt.
Gate (from the kit brief): UTF-8 text, 1 to 140 characters,
not only whitespace. The program validates the gate before writing.
"""

import os

ENTRY = 'I hired an AI agent to save me time, and now I spend all my time explaining to it what "done" means.'

MAX_CHARS = 140


def validate(text):
    """Gate from the kit brief, enforced before any write.

    One line, UTF-8, 1-140 characters, not only whitespace.
    """
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"entry is {len(text)} chars, gate is 1-{MAX_CHARS}")
    text.encode("utf-8")  # gate: must be UTF-8
    return text


def main():
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
