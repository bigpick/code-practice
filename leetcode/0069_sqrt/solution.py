#!/usr/bin/env python3

# Given a non-negative integer x, return the square root of x rounded down to the
# nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


TEST_CASES = [(4, 2), (8, 2), (10, 3), (100, 10), (1, 1), (2, 1), (3, 1), (2147395600, 46340)]


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        i = 1
        while i * i <= x:
            i += 1

        return i - 1


for test_case in TEST_CASES:
    assert Solution().mySqrt(test_case[0]) == test_case[1]
