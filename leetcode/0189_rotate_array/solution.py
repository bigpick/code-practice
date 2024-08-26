#!/usr/bin/env python3

# Given an integer array nums, rotate the array to the right by k steps,
# where k is non-negative.

TEST_CASES = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([1, 2], 5, [2, 1]),
]


class Solution:
    # def rotate_via_new_list(self, nums: list[int], k: int) -> list[int]:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     og_size = len(nums)
    #     new_list = [1]*og_size
    #     for idx, n in enumerate(nums):
    #         new_list[(idx+k)%og_size] = n
    #     return new_list

    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        pivot_pt = len(nums) - k
        nums[:] = nums[pivot_pt:] + nums[:pivot_pt]


for test_case in TEST_CASES:
    Solution().rotate(test_case[0], test_case[1])
    assert test_case[0] == test_case[2]
