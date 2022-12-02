#!/usr/bin/env python

import aoc

TOTAL_DAYS = 2

def main():
    # I wouldn't every do this normally, and this is yucky, but
    # since this is just a dumb little programming challenge calendar,
    # oh well :shrug:
    for day in range(1, TOTAL_DAYS+1):
        __import__(f"aoc.day{day:02}")
        getattr(aoc, f"day{day:02}").main()


if __name__ == "__main__":
    main()
