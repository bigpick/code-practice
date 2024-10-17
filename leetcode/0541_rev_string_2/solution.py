#!/usr/bin/env python3

# Given a string s and an integer k, reverse the first k characters for every 2k
# characters counting from the start of the string.
#
# If there are fewer than k characters left, reverse all of them. If there are less
# than 2k but greater than or equal to k characters, then reverse the first k
# characters and leave the other as original.

TEST_CASES = [
    ("abcdefg", 2, "bacdfeg"),
    ("abcd", 2, "bacd"),
    ("a", 1, "a"),
    ("abcdefg", 1, "abcdefg"),
]


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s[::-1]

        ret = ""
        for start in range(0, len(s), 2 * k):
            ret += s[start : start + k][::-1] + s[start + k : start + (k * 2)]
        return ret


for test_case in TEST_CASES:
    assert Solution().reverseStr(test_case[0], test_case[1]) == test_case[2]
