#!/usr/bin/env python3

TEST_CASES=[
    ("11", "1", "100"),
    ("1010", "1011", "10101")
]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])

for test_case in TEST_CASES:
    assert Solution().addBinary(test_case[0], test_case[1]) == test_case[2]
