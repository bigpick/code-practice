#!/usr/bin/env python

from aoc.day01 import EXAMPLE_INPUT, rank_elves


def test_rank_elves():
    assert rank_elves(EXAMPLE_INPUT) == 24000
    assert rank_elves(EXAMPLE_INPUT, 2) == 35000
    assert rank_elves(EXAMPLE_INPUT, len(EXAMPLE_INPUT)) == sum(
        list(map(int, EXAMPLE_INPUT.split()))
    )
