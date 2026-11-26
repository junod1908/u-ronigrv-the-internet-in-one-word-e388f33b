"""The Internet in One Word — one word for the whole internet.

Writes the entry to /output/entry.txt (1-30 characters, UTF-8).

The word is "actually": the whole internet is one long correction.
Every thread, reply and comment section is somebody opening with
"Actually, ..." — funny by itself, true of the internet as a whole,
surprising, and it lands in a single beat.
"""

ENTRY = "actually"

assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Self-check: what the grader reads back must be exactly the word.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", f"unexpected entry content: {written!r}"
    assert 1 <= len(written.strip()) <= 30, "entry must be 1-30 characters"


if __name__ == "__main__":
    main()
