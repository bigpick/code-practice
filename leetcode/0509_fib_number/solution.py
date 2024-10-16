#!/usr/bin/env python3

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci
# sequence, such that each number is the sum of the two preceding ones, starting
# from 0 and 1. That is,
#
#   F(0) = 0, F(1) = 1
#   F(n) = F(n - 1) + F(n - 2), for n > 1
#
# Given n, calculate F(n).
from typing import Optional

TEST_CASES = [(2, 1), (3, 2), (4, 3)]


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

    def fib_with_memo(self, n: int, vals: Optional[dict[int, int]] = None) -> int:
        if vals is None:
            vals = {}
        if n in vals:
            return vals[n]

        if n == 0 or n == 1:
            return n

        solution = self.fib_with_memo(n - 1, vals) + self.fib_with_memo(n - 2, vals)
        vals[n] = solution
        return solution


for test_case in TEST_CASES:
    assert Solution().fib(test_case[0]) == test_case[1]
    assert Solution().fib_with_memo(test_case[0]) == test_case[1]
