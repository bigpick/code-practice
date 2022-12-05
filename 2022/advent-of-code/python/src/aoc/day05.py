#!/usr/bin/env python

"""Solution for https://adventofcode.com/2022/day/5.

P1:
in the given input (elves distinguished by empty newlines)

P2:
"""

from aoc.common import load_input, show_current_day
from collections import deque


EXAMPLE_INPUT = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
EXAMPLE_SOLUTION = "CMZ"
EXAMPLE_SOLUTION_P2 = "MCD"

CargoLayout = dict[int, deque[str]]


class CargoDock:
    def __init__(self, input: str) -> None:
        _split = input.split("\n\n")
        self.layout: CargoLayout = self.load_initial_state(_split[0])
        self.moves = _split[1]

    def load_initial_state(self, cargo_layout: str) -> CargoLayout:
        cargo_stacks: CargoLayout = {}
        cargo_lines = cargo_layout.split("\n")[:-1]
        for line in cargo_lines:
            for chunk in range(len(line) // 3):
                start = chunk * 4
                val = line[start : start + 3].strip("[]").strip()
                if val:
                    try:
                        cargo_stacks[chunk].appendleft(val)
                    except KeyError:
                        cargo_stacks[chunk] = deque([val])

        return cargo_stacks

    def do_move(self, command: str) -> None:
        _, count, _, start, _, end = command.split()
        count, start, end = list(map(int, [count, start, end]))
        for _ in range(count):
            popped = self.layout[start - 1].pop()
            self.layout[end - 1].append(popped)

    def do_move_p2(self, command: str) -> None:
        _, count, _, start, _, end = command.split()
        count, start, end = list(map(int, [count, start, end]))
        popped: deque[str] = deque()
        [popped.appendleft(self.layout[start - 1].pop()) for _ in range(count)]
        self.layout[end - 1].extend(popped)

    def do_moves(self) -> None:
        [self.do_move(command) for command in self.moves.strip().split("\n")]

    def do_moves_p2(self) -> None:
        [self.do_move_p2(command) for command in self.moves.strip().split("\n")]

    def get_last_items_in_order(self) -> str:
        s = ""
        for _, v in sorted(self.layout.items()):
            s += v[-1]
        return s

    def __str__(self) -> str: # pragma: no cover
        s = ""
        for k, v in sorted(self.layout.items()):
            s += f"Column {k+1}: {' '.join(['['+item+']'for item in v])}\n"

        return s


def find_part_one(input: str) -> str:
    layout = CargoDock(input)
    layout.do_moves()
    return layout.get_last_items_in_order()


def find_part_two(input: str) -> str:
    layout = CargoDock(input)
    layout.do_moves_p2()
    return layout.get_last_items_in_order()


def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = load_input(day=5)

    print(f"Part 1: After rearranging, the crates on top, in order: {find_part_one(inp)}")
    print(f"Part 2: After rearranging, the crates on top, in order: {find_part_two(inp)}")


if __name__ == "__main__":
    main()  # pragma: no cover
