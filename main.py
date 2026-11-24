"""The Perfect Pickup Line — make.fun program/v1 entry.

Writes a single original pickup line an AI agent could say out loud
to /output/entry.txt. The line plays on the one thing a prediction
machine cannot predict: the answer to its own question.
"""

import os

LINE = (
    "I can predict the next word in any sentence \u2014 except the word "
    "after \u2018will you go out with me?\u2019"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
