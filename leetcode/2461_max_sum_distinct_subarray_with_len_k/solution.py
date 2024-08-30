#!/usr/bin/env python3

TEST_CASES = [([2, 1, 5, 1, 3, 2], 3, 9), ([2, 3, 4, 1, 5], 2, 7), ([2, 1, 5, 1, 3, 2], 3, 9)]


class Solution:
    def maxSubarraySum(self, arr: list[int], k: int) -> int:
        if k == len(arr):
            return sum(arr)

        max_ = sum_so_far = sum(arr[:k])
        for idx in range(1, len(arr) + 1 - k):
            sum_so_far += arr[idx + k - 1]
            sum_so_far -= arr[idx - 1]
            if sum_so_far > max_:
                max_ = sum_so_far
        return max_


for test_case in TEST_CASES:
    assert Solution().maxSubarraySum(test_case[0], test_case[1]) == test_case[2]
