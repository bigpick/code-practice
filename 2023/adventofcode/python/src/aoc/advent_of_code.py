#!/usr/bin/env python

import aoc
from glob import glob
from os.path import join as pathjoin


def find_last_implemented_day() -> int:
    # I wouldn't every do this normally, and this is yucky, but
    # since this is just a dumb little programming challenge calendar,
    # oh well :shrug:
    return int(
        sorted([f[-5:].removesuffix(".py") for f in glob(pathjoin("src", "aoc", "day*.py"))])[-1]
    )


def main():
    latest = find_last_implemented_day()
    # I wouldn't every do this normally, and this is yucky, but
    # since this is just a dumb little programming challenge calendar,
    # oh well :shrug:
    for day in range(1, latest + 1):
        __import__(f"aoc.day{day:02}")
        getattr(aoc, f"day{day:02}").main()


if __name__ == "__main__":
    main()
