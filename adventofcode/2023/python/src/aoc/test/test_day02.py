#!/usr/bin/env python

from aoc.day02 import (
    EXAMPLE_INPUT,
    EXAMPLE_SOLUTION,
    EXAMPLE_SOLUTION_P2,
    find_part_one,
    find_part_two,
)

INPUT = [line.strip() for line in EXAMPLE_INPUT.split("\n")]


def test_part_one():
    assert find_part_one(INPUT) == EXAMPLE_SOLUTION


def test_part_two():
    assert find_part_two(INPUT) == EXAMPLE_SOLUTION_P2
