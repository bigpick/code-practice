#!/usr/bin/env python

from __future__ import annotations

from typing import Iterable

# You are given a string s consisting of n characters which are either
# 'X' or 'O'.
#
# A move is defined as selecting three consecutive characters of s and
# converting them to 'O'. Note that if a move is applied to the
# character 'O', it will stay the same.
#
# Return the minimum number of moves required so that all the
# characters of s are converted to 'O'.


TESTS_INPUT = [("XXX", 1), ("XXOX", 2), ("OOOO", 0), ("XXOXOXOO", 2)]


class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = idx = 0
        while idx < len(s):
            if s[idx] == "O":
                idx += 1
                continue
            # now we know we've hit an X, we have to go up two more places,
            # assume all will be flipped to X (so increment the 'moves'
            # counter), and then proceed
            idx += 3
            moves += 1

        return moves


for test_case in TESTS_INPUT:
    assert Solution().minimumMoves(test_case[0]) == test_case[1]
