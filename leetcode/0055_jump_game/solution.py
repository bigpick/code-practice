#!/usr/bin/env python

# You are given an integer array nums. You are initially positioned at the array's
# first index, and each element in the array represents your maximum jump
# length at that position.
#
# Return true if you can reach the last index, or false otherwise.

TESTS_INPUT = [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([2, 5, 0, 0], True),
    ([2, 0, 0], True),
    ([3, 0, 8, 2, 0, 0, 1], True),
    ([2, 0], True),
    ([1, 1, 1, 0], True),
    ([2, 0, 1, 1, 2, 1, 0, 0, 0], False),
    ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], True),
]


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        gas = 0
        for num in nums:
            if gas < 0:
                return False
            elif num > gas:
                gas = num
            gas -= 1

        return True


for test_case in TESTS_INPUT:
    print(test_case[0])
    assert Solution().canJump(test_case[0]) == test_case[1]
