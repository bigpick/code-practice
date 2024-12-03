#!/usr/bin/env python

"""Solution for https://adventofcode.com/2024/day/2."""

from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()
EXAMPLE_INPUT_ANS = 2

EXAMPLE_INPUT_2 = EXAMPLE_INPUT
EXAMPLE_INPUT_2_ANS = 4


def split_input_to_reports(inp: str) -> list[int]:
    return [list(map(int, l.split())) for l in inp.split("\n")]


def is_safe(chall: list[int]) -> bool:
    paired = list(zip(chall, chall[1:]))
    is_monotonic = all(x > y for x, y in paired) or all(x < y for x, y in paired)
    within_1_to_3 = all(0 < abs(x - y) <= 3 for x, y in paired)
    return bool(is_monotonic and within_1_to_3)


def is_safe_part_one(chall: list[int]) -> bool:
    return is_safe(chall)


def solve_part_one(inp: str) -> int:
    """."""
    return sum([1 if is_safe_part_one(chall) else 0 for chall in split_input_to_reports(inp)])


def is_safe_part_two(chall: list[int]) -> bool:
    if is_safe_part_one(chall):
        return True

    # need to try removing at most one element
    return any(is_safe_part_one(chall[:i] + chall[i + 1 :]) for i in range(len(chall)))


def solve_part_two(inp: str) -> int:
    """."""
    return sum([1 if is_safe_part_two(chall) else 0 for chall in split_input_to_reports(inp)])


def main() -> None:
    """."""
    print(show_current_day(__file__))

    inp = load_input(day=2)

    print(f"Part 1: {solve_part_one(inp)}.")
    print(f"Part 2: {solve_part_two(inp)}.")


if __name__ == "__main__":
    main()  # pragma: no cover
