#!/usr/bin/env python3

# For two strings s and t, we say "t divides s" if and only if
# s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x
# divides both str1 and str2.

from math import gcd

TEST_CASES = [
    ("ABCABC", "ABC", "ABC"),
    ("ABABAB", "ABAB", "AB"),
    ("LEET", "CODE", ""),
    ("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXX"),
]


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        max_substr = gcd(len(str1), len(str2))
        for i in range(max_substr):
            if str1[i] != str2[i]:
                return ""
        return str1[:max_substr]


for test_case in TEST_CASES:
    assert Solution().gcdOfStrings(test_case[0], test_case[1]) == test_case[2]
