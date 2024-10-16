#!/usr/bin/env python3

# Given an integer array nums, return true if there exists a triple of indices
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices
# exists, return false.


TEST_CASES = [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    ([2, 1, 5, 0, 4, 6], True),
    ([20, 100, 10, 12, 5, 13], True),
]


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return False

        low = nums[0]
        for val in nums:
            if val < low:
                low = val
            elif val > low:
                conseq += 1
        return False


for test_case in TEST_CASES:
    assert Solution().increasingTriplet(test_case[0]) == test_case[1]
