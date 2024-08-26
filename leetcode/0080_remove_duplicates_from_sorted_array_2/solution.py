#!/usr/bin/env python

# Given an integer array nums sorted in non-decreasing order, remove some duplicates
# in-place such that each unique element appears at most twice. The relative order of
# the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you
# must instead have the result be placed in the first part of the array nums. More
# formally, if there are k elements after removing the duplicates, then the first k
# elements of nums should hold the final result. It does not matter what you leave
# beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums
#
# Do not allocate extra space for another array. You must do this by modifying the
# input array in-place with O(1) extra memory.

TESTS_INPUT = [
    ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3, -1]),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3, -1, -1]),
]


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        idx = 0

        for item in nums:
            if idx < 2 or item != nums[idx - 2]:
                nums[idx] = item
                idx += 1

        return idx


for test_case in TESTS_INPUT:
    ans = Solution().removeDuplicates(test_case[0])
    print(ans)
    assert ans == test_case[1]
    assert test_case[0][: test_case[1]] == test_case[2][: test_case[1]]
