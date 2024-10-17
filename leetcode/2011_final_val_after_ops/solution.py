#!/usr/bin/env python3

# There is a programming language with only four operations and one variable X:
#
#     ++X and X++ increments the value of the variable X by 1.
#     --X and X-- decrements the value of the variable X by 1.
#
# Initially, the value of X is 0.
#
# Given an array of strings operations containing a list of operations, return
# the final value of X after performing all the operations.

TEST_CASES = [
    (["--X", "X++", "X++"], 1),
    (["++X", "++X", "X++"], 3),
    (["X++", "++X", "--X", "X--"], 0),
]


class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        val = 0
        ops = {
            "--X": lambda x: x - 1,
            "X--": lambda x: x - 1,
            "X++": lambda x: x + 1,
            "++X": lambda x: x + 1,
        }
        for op in operations:
            val = ops[op](val)
        return val


for test_case in TEST_CASES:
    assert Solution().finalValueAfterOperations(test_case[0]) == test_case[1]
