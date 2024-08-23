#!/usr/bin/env python

from aoc.day03 import (
    EXAMPLE_INPUT,
    EXAMPLE_SOLUTION,
    EXAMPLE_SOLUTION_P2,
    find_priority_of_3sum,
    find_priority_sum_each_rucksack,
)


def test_part_one():
    assert find_priority_sum_each_rucksack(EXAMPLE_INPUT.split()) == EXAMPLE_SOLUTION


def test_part_two():
    assert find_priority_of_3sum(EXAMPLE_INPUT.split()) == EXAMPLE_SOLUTION_P2
