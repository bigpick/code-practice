#!/usr/bin/env python3

# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1
# means not empty, and an integer n, return true if n new flowers can be
# planted in the flowerbed without violating the no-adjacent-flowers rule and
# false otherwise.

TEST_CASES = [
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False),
    ([1, 0, 1, 0, 1], 1, False),
    ([], 1, False),
    ([0, 0, 0, 0], 2, True),
    ([0, 0, 0, 0], 3, False),
    ([0, 0, 0, 0, 0], 3, True),
    ([1, 0, 0, 0, 0, 1], 2, False),
    ([0], 1, True),
    ([1], 0, True),
]


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) == 0:
            return False
        elif len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            return n == 1

        spaces = 0
        last_seen = flowerbed[0]
        if last_seen == 0 and flowerbed[1] == 0:
            spaces += 1
            last_seen = 1

        for idx in range(1, len(flowerbed)):
            current = flowerbed[idx]
            if idx < len(flowerbed) - 1:
                next_ = flowerbed[idx + 1]
            if last_seen == current == next_ == 0:
                spaces += 1
                last_seen = 1
            else:
                last_seen = current

        return spaces >= n


for test_case in TEST_CASES:
    assert Solution().canPlaceFlowers(test_case[0], test_case[1]) == test_case[2]
