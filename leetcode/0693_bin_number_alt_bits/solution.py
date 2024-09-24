#!/usr/bin/env python3

# Given a positive integer, check whether it has alternating bits: namely, if two
# adjacent bits will always have different values.

TEST_CASES = [
    (5, True),  # 101
    (7, False),  # 111
    (11, False),  # 1011
]


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_ = bin(n)[2:]
        last = bin_[0]
        for val in bin_[1:]:
            if val == last:
                return False
            last = val

        return True


for test_case in TEST_CASES:
    assert Solution().hasAlternatingBits(test_case[0]) == test_case[1]
