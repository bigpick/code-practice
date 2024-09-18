#!/usr/bin/env python3

# Given a list of non-negative integers nums, arrange them such that they form the
# largest number and return it.
#
# Since the result may be very large, so you need to return a string instead
# of an integer.

TEST_CASES = [([10, 2], "210"), ([3, 30, 34, 5, 9], "9534330"), ([0, 0, 0], "0"), ([0], "0")]


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        from functools import cmp_to_key

        def compare_two_number_strings(left: str, right: str) -> int:
            if left + right < right + left:
                return 1
            return -1

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare_two_number_strings))
        if nums[0] == "0":
            return "0"

        return "".join(nums)


for test_case in TEST_CASES:
    assert Solution().largestNumber(test_case[0]) == test_case[1]
