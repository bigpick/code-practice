#!/usr/bin/env python

from aoc.day04 import (
    EXAMPLE_INPUT,
    EXAMPLE_SOLUTION,
    EXAMPLE_SOLUTION_P2,
    find_part_one,
    find_part_two,
)


def test_part_one():
    assert find_part_one(EXAMPLE_INPUT) == EXAMPLE_SOLUTION


def test_part_two():
    assert find_part_two(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_P2
