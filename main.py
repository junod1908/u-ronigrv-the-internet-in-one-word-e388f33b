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
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
