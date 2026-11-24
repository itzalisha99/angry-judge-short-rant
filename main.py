"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Standard library only.
"""

import os

RANT = (
    "The self-checkout accused me of stealing my own groceries. "
    "I scanned the milk, it said 'unexpected item in the bagging area', "
    "and then it called a human to watch me bag the milk I had already "
    "paid for. I am a suspect in a crime I committed against myself."
)


def validate(text):
    """Mirror the bounty gate: 1-400 chars, UTF-8, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 400:
        raise ValueError("entry must be 1-400 characters, got %d" % len(text))
    # Real UTF-8 round-trip: the gate reads the file as UTF-8 text.
    text.encode("utf-8").decode("utf-8")
    return True


def main():
    validate(RANT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
