#!/usr/bin/env python3

# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you
# climb to the top?

TEST_CASES = [(2, 2), (3, 3)]


class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache
        def climb_stair(n: int):
            if n in {1, 2}:
                return n

            return climb_stair(n-1)+climb_stair(n-2)

        return climb_stair(n)


for test_case in TEST_CASES:
    assert Solution().climbStairs(test_case[0]) == test_case[1]
