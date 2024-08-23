#!/usr/bin/env python

from aoc.day02 import EXAMPLE_INPUT, EXAMPLE_SOLUTION, EXAMPLE_SOLUTION_P2
from aoc.day02 import RockPaperScissorsGame, FixedRPSGame


def test_rps_partone():
    assert RockPaperScissorsGame.from_str(EXAMPLE_INPUT.strip()) == EXAMPLE_SOLUTION


def test_rps_parttwo():
    assert FixedRPSGame.from_str(EXAMPLE_INPUT.strip()) == EXAMPLE_SOLUTION_P2
