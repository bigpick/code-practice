#!/usr/bin/env python3

# You have a bomb to defuse, and your time is running out! Your informer will provide you
# with a circular array code of length of n and a key k.
#
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
#
#     If k > 0, replace the ith number with the sum of the next k numbers.
#     If k < 0, replace the ith number with the sum of the previous k numbers.
#     If k == 0, replace the ith number with 0.
#
# As code is circular, the next element of code[n-1] is code[0], and the previous element
# of code[0] is code[n-1].
#
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

TEST_CASES = [
    ([5, 7, 1, 4], 3, [12, 10, 16, 13]),
    ([1, 2, 3, 4], 0, [0, 0, 0, 0]),
    ([2, 4, 9, 3], -2, [12, 5, 6, 13]),
]


class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        if k == 0:
            return [0] * len(code)

        pass


for test_case in TEST_CASES:
    assert Solution().decrypt(test_case[0], test_case[1]) == test_case[2]
