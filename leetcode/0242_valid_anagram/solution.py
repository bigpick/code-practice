#!/usr/bin/env python3

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

TEST_CASES = [("anagram", "nagaram", True), ("rat", "car", False)]


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


for test_case in TEST_CASES:
    assert Solution().isAnagram(test_case[0], test_case[1]) == test_case[2]
