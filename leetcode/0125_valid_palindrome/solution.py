#!/usr/bin/env python3

# A phrase is a palindrome if, after converting all uppercase letters into lowercase
# letters and removing all non-alphanumeric characters, it reads the same forward and
# backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

TEST_CASES = [("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string

        s = s.translate(str.maketrans("", "", string.punctuation)).strip().replace(" ", "").lower()
        return s == s[::-1]


for test_case in TEST_CASES:
    assert Solution().isPalindrome(test_case[0]) == test_case[1]
