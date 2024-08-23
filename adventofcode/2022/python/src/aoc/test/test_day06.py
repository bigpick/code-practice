#!/usr/bin/env python

from aoc.day06 import (
    EXAMPLE_INPUT,
    EXAMPLE_SOLUTIONS,
    EXAMPLE_SOLUTIONS_P2,
    find_part_one,
    find_part_two,
)


def test_part_one():
    for idx, f in enumerate(EXAMPLE_INPUT.split()):
        assert find_part_one(f) == EXAMPLE_SOLUTIONS[idx]


def test_part_two():
    for idx, f in enumerate(EXAMPLE_INPUT.split()):
        assert find_part_two(f) == EXAMPLE_SOLUTIONS_P2[idx]
