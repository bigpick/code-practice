#!/usr/bin/env python
from __future__ import annotations

"""Solution for https://adventofcode.com/2022/day/8.

P1: How many trees are visible from outside the grid?

Trees are visible if they are:
    * the ottermost tree in the grid, i.e row 0 or N, or col 0 or N
    * surrounded by any tree on their exterior that is strictly < their
      current height in N/E/S/W all the way to the border

P2: What is the highest scenic score possible for any tree?

Scenic score is calculated by multiplying the "viewing distance" in
each direction for a given tree, which is the number of trees that are
able to be seen before being blocked in one direction.
"""

from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """30373
25512
65332
33549
35390"""
EXAMPLE_SOLUTION = 21
EXAMPLE_SOLUTION_P2 = 8


def get_slice_to_n_border(curr_row: int, curr_col: int, trees: list[str]) -> list[int]:
    return list(map(int, [trees[i][curr_col] for i in range(curr_row - 1, -1, -1)]))


def get_slice_to_s_border(curr_row: int, curr_col: int, trees: list[str]) -> list[int]:
    return list(map(int, [trees[i][curr_col] for i in range(curr_row + 1, len(trees))]))


def get_slice_to_e_border(curr_row: int, curr_col: int, trees: list[str]) -> list[int]:
    l = len(trees[0])
    return list(map(int, [trees[curr_row][col] for col in range(curr_col + 1, l)]))


def get_slice_to_w_border(curr_row: int, curr_col: int, trees: list[str]) -> list[int]:
    return list(map(int, [trees[curr_row][col] for col in range(curr_col - 1, -1, -1)]))


def is_visible_from_outside(height: int, trees_to_border: list[int]) -> bool:
    return all([height > tree for tree in trees_to_border])


def get_scenic_score(height: int, neighbors: list[int]) -> int:
    scenic_score = 0
    for tree in neighbors:
        if tree < height:
            scenic_score += 1
        elif tree >= height:
            scenic_score += 1
            return scenic_score
    return scenic_score


def get_viewing_distance(height: int, row: int, col: int, lines: list[str]):
    neighbors = [
        get_slice_to_n_border(row, col, lines),
        get_slice_to_s_border(row, col, lines),
        get_slice_to_e_border(row, col, lines),
        get_slice_to_w_border(row, col, lines),
    ]

    from math import prod

    return prod([get_scenic_score(height, neighbor_list) for neighbor_list in neighbors])


def check_neighbors(height: int, row: int, col: int, lines: list[str]):
    neighbors = [
        get_slice_to_n_border(row, col, lines),
        get_slice_to_s_border(row, col, lines),
        get_slice_to_e_border(row, col, lines),
        get_slice_to_w_border(row, col, lines),
    ]
    if any(is_visible_from_outside(height, trees_to_border) for trees_to_border in neighbors):
        return 1
    return 0


def find_part_one(input: str):
    lines = input.split("\n")
    rows = len(lines)
    cols = len(lines[0])

    visible = (2 * cols) + (2 * rows) - 4
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            visible += check_neighbors(int(lines[row][col]), row, col, lines)
    return visible


def find_part_two(input: str):
    lines = input.split("\n")
    rows = len(lines)
    cols = len(lines[0])

    max_score = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            s = get_viewing_distance(int(lines[row][col]), row, col, lines)
            if s > max_score:
                max_score = s
    return max_score


def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = load_input(day=8)

    print(f"Part 1: {find_part_one(EXAMPLE_INPUT)}")
    print(f"Part 1: Total number of trees visible from outside: {find_part_one(inp)}")
    print(f"Part 2: Total highest possible scenic score possible: {find_part_two(inp)}")


if __name__ == "__main__":
    main()  # pragma: no cover
