#!/usr/bin/env python

"""Common utilities for all Advent of Code modules."""

from os.path import join as pathjoin


def show_current_day(fname: str):
    f = fname.split("/")[-1].removesuffix(".py")
    return f"====== {f} ======"


def load_input(day: int) -> str:
    with open(pathjoin("src", "aoc", "inputs", f"day_{day:02}.txt"), "r") as infile:
        return infile.read().rstrip()
