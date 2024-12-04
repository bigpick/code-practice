#!/usr/bin/env python

from aoc.day04 import (
    EXAMPLE_INPUT,
    EXAMPLE_INPUT_2,
    EXAMPLE_INPUT_2_ANS,
    EXAMPLE_INPUT_ANS,
    solve_part_one,
    solve_part_two,
)


def test_part_one():
    assert solve_part_one(EXAMPLE_INPUT, ["XMAS"]) == EXAMPLE_INPUT_ANS


def test_part_two():
    assert solve_part_two(EXAMPLE_INPUT_2) == EXAMPLE_INPUT_2_ANS
