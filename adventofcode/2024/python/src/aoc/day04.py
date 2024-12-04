#!/usr/bin/env python

"""Solution for https://adventofcode.com/2024/day/4 ."""

from enum import Enum

from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()
EXAMPLE_INPUT_ANS = 18

EXAMPLE_INPUT_2 = EXAMPLE_INPUT
EXAMPLE_INPUT_2_ANS = 9


class Directions(Enum):
    up = 1
    down = 2
    left = 3
    right = 4
    diag_up_left = 5
    diag_up_right = 6
    diag_down_left = 7
    diag_down_right = 8


def search_direction(
    y: int, x: int, word: list[str], lines: list[str], direction: int
) -> tuple[bool, list[tuple[int, int]]]:
    idx = 0
    visited = []

    while (
        idx <= len(word) - 1
        and 0 <= y <= len(lines) - 1
        and 0 <= x <= len(lines[y]) - 1
        and lines[y][x] == word[idx]
    ):
        visited.append((x, y, word[idx]))
        idx += 1
        match direction:
            case Directions.up:
                y -= 1
            case Directions.down:
                y += 1
            case Directions.right:
                x += 1
            case Directions.left:
                x -= 1
            case Directions.diag_up_right:
                x += 1
                y -= 1
            case Directions.diag_up_left:
                x -= 1
                y -= 1
            case Directions.diag_down_right:
                x += 1
                y += 1
            case Directions.diag_down_left:
                x -= 1
                y += 1
            case _:
                raise RuntimeError("Wrong direction?")

    if idx == len(word):
        print(f"{direction} found to be valid, {visited}")
        return True, visited

    return False, []


def solve_part_one(inp: str, words: list[str]) -> int:
    """."""
    lines = inp.split("\n")
    height = len(lines)
    width = len(lines[0])
    print(height, width)
    total = 0
    x = y = 0

    matched = []
    for _ in range(height):
        matched.append(list("*") * width)

    print()

    for word in words:
        word = list(word)

        for yy in range(height):
            for xx in range(width + 1):
                for direction in Directions:
                    valid, coords = search_direction(yy, xx, word, lines, direction)
                    if valid:
                        total += 1
                        for x, y, l in coords:
                            matched[y][x] = l

    print("\n".join("".join(line) for line in matched))
    return total


def is_valid_x_mas(x: int, y: int, lines: list[str]) -> bool:
    top_left = lines[y - 1][x - 1]
    top_right = lines[y - 1][x + 1]
    bot_left = lines[y + 1][x - 1]
    bot_right = lines[y + 1][x + 1]
    vals = {"M", "S"}

    return bool(
        top_left != bot_right
        and top_left in vals
        and top_right in vals
        and top_right != bot_left
        and bot_left in vals
        and bot_right in vals
    )


def solve_part_two(inp: str) -> int:
    """."""
    lines = inp.split("\n")
    height = len(lines)
    width = len(lines[0])
    print(height, width)
    total = 0
    x = y = 0

    matched = []
    for _ in range(height):
        matched.append(list("*") * width)

    print()
    for y in range(1, height - 1):
        for x in range(1, len(lines[y]) - 1):
            if lines[y][x] != "A":
                continue

            if is_valid_x_mas(x, y, lines):
                total += 1
                matched[y][x] = lines[y][x]

    print("\n".join("".join(line) for line in matched))
    return total


def main() -> None:
    """."""
    print(show_current_day(__file__))

    inp = load_input(day=4)

    print(f"Part 1: {solve_part_one(inp, ["XMAS"])}")
    print(f"Part 2: {solve_part_two(inp)}")


if __name__ == "__main__":
    main()  # pragma: no cover
