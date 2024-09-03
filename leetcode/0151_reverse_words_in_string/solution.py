#!/usr/bin/env python3

# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will be
# separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words.
#
# Do not include any extra spaces.


TEST_CASES = [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("the", "the"),
    ("a good   example", "example good a"),
]


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            left += 1
            right -= 1

        return " ".join(s)


for test_case in TEST_CASES:
    assert Solution().reverseWords(test_case[0]) == test_case[1]
