#!/usr/bin/env python3

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


TEST_CASES = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("", "abc", True),
    ("abc", "", False),
    ("acb", "ahbgdc", False),
    ("aaaaaa", "bbaaaa", False),
]


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) != 0 and len(t) == 0:
            return False

        left = right = 0
        while left < len(s):
            if right >= len(t):
                return False

            if s[left] == t[right]:
                left += 1

            right += 1

        return left == len(s)


for test_case in TEST_CASES:
    assert Solution().isSubsequence(test_case[0], test_case[1]) == test_case[2]
