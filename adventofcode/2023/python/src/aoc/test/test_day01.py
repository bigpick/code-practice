#!/usr/bin/env python

from aoc.day01 import EXAMPLE_INPUT, get_calibration


def test_get_calibration():
    assert get_calibration(EXAMPLE_INPUT) == 142
