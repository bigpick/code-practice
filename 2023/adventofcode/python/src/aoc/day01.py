#!/usr/bin/env python

"""Solution for https://adventofcode.com/2023/day/1.

P1: What is the sum of all of the calibration values?

P2: What is the sum of all of the calibration values? now numbers can
appear in both numeric form 1,2,3 and 'word' form 'one, two, three'.
"""

from aoc.common import load_input, show_current_day
from re import sub

EXAMPLE_INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

EXAMPLE_INPUT_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

NUM_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def replace_digit_words(line: str) -> str:
    for k,v in NUM_MAP.items():
        line = sub(k, k[0]+v+k[-1], line)
    return line


def get_calibration(calibration_values: str, allow_non_nums: bool = False) -> int:
    sum = 0
    for line in calibration_values.split("\n"):
        if allow_non_nums:
            line = replace_digit_words(line)

        line = sub("[^0-9]", "", line)

        if len(line) == 1:
            sum += int(line[0] + line[0])
        else:
            sum += int(line[0] + line[-1])

    return sum


def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = load_input(day=1)
    print(f"Part 1: Sum of all calibration values: {get_calibration(inp)}.")
    print(f"Part 2: Sum of all calibration values: {get_calibration(inp, True)}.")


if __name__ == "__main__":
    main()  # pragma: no cover
