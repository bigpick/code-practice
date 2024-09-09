#!/usr/bin/env python3

# Given an binary array nums and an integer k, return true if all 1's are at least k
# places away from each other, otherwise return false.
TEST_CASES = [
    ([1, 0, 0, 0, 1, 0, 0, 1], 2, True),
    ([1, 0, 0, 1, 0, 1], 2, False),
    ([0,1,0,0,1,0,0,1], 2, True),
    ([0,0,0], 2, True),
]


class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        current = 0

        while nums[current] != 1 and current < len(nums)-1:
            current += 1

        if current == len(nums):
            return True

        next_ = current+1
        while next_ < len(nums):
            if nums[next_] == 1:
                if next_ - current <= k:
                    return False
                current = next_

            next_ += 1


        return True

for test_case in TEST_CASES:
    assert Solution().kLengthApart(test_case[0], test_case[1]) == test_case[2]
