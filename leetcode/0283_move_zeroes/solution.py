#!/usr/bin/env python3

# Given an integer array nums, move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

TEST_CASES = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([1, 0], [1, 0]),
    ([1, 0, 0], [1, 0, 0]),
]


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        while left < len(nums) - 1:
            if nums[left] == 0:
                while nums[right] == 0 and right < len(nums) - 1:
                    right += 1

                nums[left] = nums[right]
                nums[right] = 0

            left += 1
            right = left

        print(nums)


for test_case in TEST_CASES:
    Solution().moveZeroes(test_case[0])
    assert test_case[0] == test_case[1]
