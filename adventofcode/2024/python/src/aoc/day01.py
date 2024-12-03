#!/usr/bin/env python

"""Solution for https://adventofcode.com/2024/day/1.

P1:  What is the total distance between your lists?

P2: What is the sum of all of the calibration values? now numbers can
appear in both numeric form 1,2,3 and 'word' form 'one, two, three'.
"""

from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()
EXAMPLE_INPUT_ANS = 11

EXAMPLE_INPUT_2 = EXAMPLE_INPUT
EXAMPLE_INPUT_2_ANS = 31


def split_input_to_sorted_lists(inp: str) -> tuple[list[int], list[int]]:
    """."""
    left = []
    right = []

    for p in inp.split("\n"):
        l, r = map(int, p.split())
        left.append(l)
        right.append(r)

    return sorted(left), sorted(right)


def try_add(d: dict[str, int], val: str) -> None:
    try:
        d[val] += 1
    except KeyError:
        d[val] = 1


def solve_part_one(inp: str) -> int:
    """."""
    left, right = split_input_to_sorted_lists(inp)
    if len(left) != len(right):
        raise RuntimeError("Lengths not equal")

    diff = 0
    for i in range(len(left)):
        diff += abs(left[i] - right[i])

    return diff


def solve_part_two(inp: str) -> int:
    """."""
    left = {}
    right = {}
    for p in inp.split("\n"):
        l, r = p.split()
        try_add(left, l)
        try_add(right, r)

    diff = 0
    for val, count in left.items():
        if val in right:
            diff += int(val) * right[val] * count

    return diff


def main() -> None:
    """."""
    print(show_current_day(__file__))

    inp = load_input(day=1)

    print(f"Part 1: {solve_part_one(inp)}.")
    print(f"Part 2: {solve_part_two(inp)}.")


if __name__ == "__main__":
    main()  # pragma: no cover
