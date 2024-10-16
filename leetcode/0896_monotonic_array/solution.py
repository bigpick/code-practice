#!/usr/bin/env python3

TEST_CASES = [
    ([1, 2, 2, 3], True),
    ([6, 5, 4, 4], True),
    ([1, 3, 2], False),
    ([1, 1, 0], True),
    (
        [
            1,
            1,
            1,
        ],
        True,
    ),
]


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) in (0, 1, 2):
            return True

        start, next_ = 0, 1
        while nums[start] == nums[next_] and next_ < len(nums) - 1:
            start, next_ = start + 1, next_ + 1

        first = nums[start]
        last = nums[next_]

        mono = "dec" if first > last else "inc"

        for val in nums[next_ + 1 :]:
            if val > last and mono == "dec" or val < last and mono == "inc":
                return False

            last = val

        return True


for test_case in TEST_CASES:
    assert Solution().isMonotonic(test_case[0]) == test_case[1]
