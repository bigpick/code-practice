#!/usr/bin/env python

from aoc.common import load_input, show_current_day


def test_load_input():
    assert load_input(99) == "foofoo\n\nbarbar"


def test_show_current_day():
    assert show_current_day("foo/bar/baz/day00.py") == "====== day00 ======"
