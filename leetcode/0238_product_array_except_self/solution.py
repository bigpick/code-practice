#!/usr/bin/env python3

# Given an integer array nums, return an array answer such that answer[i] is equal to
# the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division
# operation.
#
# Follow up: Can you solve the problem in O(1) extra space complexity? The output
# array does not count as extra space for space complexity analysis.)

TEST_CASES = [([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        size_nums = len(nums)
        results = [1] * size_nums

        left_prod = 1
        for idx in range(size_nums):
            results[idx] = left_prod
            left_prod *= nums[idx]

        right_prod = 1
        for idx in range(size_nums - 1, -1, -1):
            results[idx] *= right_prod
            right_prod *= nums[idx]
        return results


for test_case in TEST_CASES:
    assert Solution().productExceptSelf(test_case[0]) == test_case[1]
