#!/usr/bin/env python

"""Solution for https://adventofcode.com/2022/day/6.

P1: How many characters need to be processed before the first
start-of-packet marker is detected (4 unique chars)?

P2: How many characters need to be processed before the first
start-of-message marker is detected (14 unique chars)?
"""

from collections.abc import Iterable
from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""
EXAMPLE_SOLUTIONS = [7, 5, 6, 10, 11]
EXAMPLE_SOLUTIONS_P2 = [19, 23, 23, 29, 26]


def sliding_windows(l: str, win_size: int) -> Iterable[tuple[int, str]]:
    for idx, i in enumerate(range(len(l) - win_size + 1)):
        yield idx, l[i : i + win_size]


def find_part_one(input: str):
    win_size = 4
    for idx, win in sliding_windows(input, win_size):
        if len(set(win)) == win_size:
            # print(idx, win)
            return idx + win_size


def find_part_two(input: str):
    win_size = 14
    for idx, win in sliding_windows(input, win_size):
        if len(set(win)) == win_size:
            # print(idx, win)
            return idx + win_size

def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = load_input(day=6)

    for idx, f in enumerate(EXAMPLE_INPUT.split()):
        assert find_part_one(f) == EXAMPLE_SOLUTIONS[idx]
        assert find_part_two(f) == EXAMPLE_SOLUTIONS_P2[idx]

    print(f"Part 1: {find_part_one(inp)}")
    print(f"Part 2: {find_part_two(inp)}")


if __name__ == "__main__":
    main()  # pragma: no cover
