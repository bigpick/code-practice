#!/usr/bin/env python3

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

TEST_CASES = [([1, 1, 0, 1, 1, 1], 3), ([1, 0, 1, 1, 0, 1], 2)]


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        so_far = max_ones = 0
        for val in nums:
            if val == 1:
                so_far += 1
            else:
                max_ones = max(max_ones, so_far)
                so_far = 0

        max_ones = max(max_ones, so_far)
        return max_ones


for test_case in TEST_CASES:
    assert Solution().findMaxConsecutiveOnes(test_case[0]) == test_case[1]
