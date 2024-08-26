#!/usr/bin/env python3

# Given an array `nums` of size `n`, return the _majority element_.
#
# The _majority element_ is the element that appears more than [n / 2] times. You
# may assume that the majority element _always_ exists in the array.
#
#  Follow-up: Could you solve the problem in linear time and in O(1) space?

TEST_CASES = [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2), ([3,3,4], 3)]


class Solution:
    def naive_majorityElement(self, nums: list[int]) -> int:
        # O(n^2)
        min_occurence = len(nums) // 2
        d = {}
        for elem in nums:
            try:
                d[elem] += 1
            except KeyError:
                d[elem] = 1

        for k, v in d.items():
            if v > min_occurence:
                return k

    def majorityElement(self, nums: list[int]) -> int:
        current_item = None
        current_count = None
        for num in nums:
            if current_item is None:
                current_item = num
                current_count = 1
                continue

            if num != current_item:
                current_count -= 1
            else:
                current_count += 1

            if current_count == 0:
                current_item = num
                current_count = 1

        return current_item


for test_case in TEST_CASES:
    print(Solution().naive_majorityElement(test_case[0]))
    assert Solution().naive_majorityElement(test_case[0]) == test_case[1]

    print(Solution().majorityElement(test_case[0]))
    assert Solution().majorityElement(test_case[0]) == test_case[1]
