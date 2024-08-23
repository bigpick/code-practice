#!/usr/bin/env python

TESTS_INPUT = [
    ([1,1,2], 2, [1,2]),
    ([0,0,1,1,1,2,2,3,3,4], 5, [0, 1, 2, 3, 4])
]


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Given an integer array nums sorted in non-decreasing order, remove the
        # duplicates in-place such that each unique element appears only once. The
        # relative order of the elements should be kept the same. Then return the
        # number of unique elements in nums.
        last_seen = None
        idx = len(nums)-1

        while idx >= 0:
            current = nums[idx]
            if current == last_seen:
                nums.pop(idx)
            idx-=1
            last_seen = current
        return len(nums)


for test_case in TESTS_INPUT:
    assert Solution().removeDuplicates(test_case[0]) == test_case[1]
    assert test_case[0] == test_case[2]
