#!/usr/bin/env python

"""Solution for https://adventofcode.com/2024/day/3 ."""

from re import compile as re_compile
from re import findall

from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".strip()
EXAMPLE_INPUT_ANS = 161

EXAMPLE_INPUT_2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip()
EXAMPLE_INPUT_2_ANS = 48


def part_one(inp: str) -> int:
    patt = re_compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    sum_ = 0
    for p in findall(patt, inp):
        sum_ += int(p[0]) * int(p[1])
    return sum_


def part_two(inp: str) -> int:
    # strip out all the stuff between don't()...do()
    patt = re_compile(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))")

    matches = findall(patt, inp)
    sum_ = 0
    enabled = True

    for token in matches:
        match token[0]:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled:
                sum_ += int(token[1]) * int(token[2])

    return sum_


def solve_part_one(inp: str) -> int:
    """."""
    return part_one(inp)


def solve_part_two(inp: str) -> int:
    """."""
    return part_two(inp)


def main() -> None:
    """."""
    print(show_current_day(__file__))

    inp = load_input(day=3)

    print(f"Part 1: {solve_part_one(inp)}")
    print(f"Part 2: {solve_part_two(inp)}")


if __name__ == "__main__":
    main()  # pragma: no cover
