#!/usr/bin/env python3

# Given an array of positive integers nums, return the maximum possible sum of an
# ascending subarray in nums.
#
# A subarray is defined as a contiguous sequence of numbers in an array.
#
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for
# all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.


TEST_CASES = [
    ([10, 20, 30, 5, 10, 50], 65),
    ([10, 20, 30, 40, 50], 150),
    ([12, 17, 15, 13, 10, 11, 12], 33),
]


class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        highest_sum = current_sum = last = 0

        for val in nums:
            if val > last:
                current_sum += val
                last = val
                continue

            highest_sum = max(current_sum, highest_sum)
            current_sum = last = val

        return max(current_sum, highest_sum)


for test_case in TEST_CASES:
    assert Solution().maxAscendingSum(test_case[0]) == test_case[1]
