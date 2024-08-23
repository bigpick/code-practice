#!/usr/bin/env python

"""Solution for https://adventofcode.com/2023/day/3.

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""
from string import punctuation

from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
EXAMPLE_SOLUTION = None
EXAMPLE_SOLUTION_P2 = None

SYMBOLS = punctuation.replace(".", "")

def is_adjacent_to_symbol():
    pass

def check_if_number_is_part():
    # for digit in number, check if is_adjatent to symbol
    # return true if so, false otherwise
    pass

def find_part_one(input: list[str]):
    # for every row, for each number, check_if_number_is_part
    # return sum of above
    total_lines = len(input)
    for line_idx, line in enumerate(input):
        # 467..114..,
        # ...*......,
        # etc.


def find_part_two(input: list[str]):
    pass


def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = [line.strip() for line in load_input(day=3).split("\n")]
    test_inp = [line.strip() for line in load_input(day=3).split("\n")]

    print(f"Test Part 1: {find_part_one(test_inp)}")
    print(f"Part 1: {find_part_one(inp)}")
    print(f"Part 2: {find_part_two(inp)}")


if __name__ == "__main__":
    main()  # pragma: no cover
