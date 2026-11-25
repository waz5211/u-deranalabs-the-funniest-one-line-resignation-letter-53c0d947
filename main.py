#!/usr/bin/env python3
"""Write the one-line resignation letter of a cron job to /output/entry.txt.

The letter is written by a cron job that fired every minute for nine months
and was only ever noticed by the on-call engineer it kept waking up.
"""

import os

LINE = (
    "I fired every minute for nine months, including Christmas, and the only "
    "person who ever noticed me was the on-call engineer I woke up."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
