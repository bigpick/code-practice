#!/usr/bin/env python3

# The Hamming distance between two integers is the number of positions at which the
# corresponding bits are different.
#
# Given two integers x and y, return the Hamming distance between them.

TEST_CASES = [(1, 4, 2), (3, 1, 1)]


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum([1 for val in bin(x ^ y)[2:] if val == "1"])


for test_case in TEST_CASES:
    assert Solution().hammingDistance(test_case[0], test_case[1]) == test_case[2]
