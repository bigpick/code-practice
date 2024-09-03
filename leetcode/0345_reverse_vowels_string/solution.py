#!/usr/bin/env python3

# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and
# upper cases, more than once.

VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

TEST_CASES = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
    ("world", "world"),
    ("good", "good"),
    ("abcdef", "ebcdaf"),
    ("fffff", "fffff"),
    ("affff", "affff"),
]


class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            while s[left] not in VOWELS and left < len(s) - 1:
                left += 1
            while s[right] not in VOWELS and right > 0:
                right -= 1

            if left >= right:
                return "".join(s)

            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            left += 1
            right -= 1

        return "".join(s)


for test_case in TEST_CASES:
    assert Solution().reverseVowels(test_case[0]) == test_case[1]
