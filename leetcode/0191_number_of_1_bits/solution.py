#!/usr/bin/env python3

# Given a positive integer n, write a function that returns the number of
# set bits in its binary representation (also known as the Hamming weight).


TEST_CASES = [
    (11, 3),
    (128, 1),
    (2147483645, 30)
]

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([1 for x in bin(n)[2:] if x == "1"])


for test_case in TEST_CASES:
    assert Solution().hammingWeight(test_case[0]) == test_case[1]
