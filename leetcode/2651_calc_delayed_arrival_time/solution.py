#!/usr/bin/env python3

TEST_CASES = [(15, 5, 20), (13, 11, 0)]


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


for test_case in TEST_CASES:
    assert Solution().findDelayedArrivalTime(test_case[0], test_case[1]) == test_case[2]
