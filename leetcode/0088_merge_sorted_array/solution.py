#!/usr/bin/env python

TESTS_INPUT = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([1, 0], 1, [2], 1, [1, 2]),
    ([2, 0], 1, [1], 1, [1, 2]),
    ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
]


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if not nums1 or not nums2:
            return

        if m == 0:
            nums1[:] = nums2
            return

        left = 0
        while left < m and nums2:
            if nums1[left] > nums2[0]:
                nums1.pop()
                nums1.insert(left, nums2.pop(0))

                if nums2:
                    m += 1

            left += 1

        if nums2:
            nums1[left:] = nums2[:]


for test_case in TESTS_INPUT:
    Solution().merge(test_case[0], test_case[1], test_case[2], test_case[3])
    print(test_case[0], test_case[4])
    assert test_case[0] == test_case[4]
