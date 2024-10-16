#!/usr/bin/env python3

# Given an array of strings `words` and a string `s`, determin if `s` is an **acronym**
# of words.
#
# The string `s` ins considered ot be an acronym of `words` if it can be formed by
# concatenating the **first** character of each string in `words` in order.
#
# e.g. "ab" can be formed from ["apple", "banana"], but not from ["bear", "aardvark"]
#
# Return true if so, false otherwise

TEST_CASES = [
    (["alice", "bob", "charlie"], "abc", True),
    (["an", "apple"], "a", False),
    (["never", "gonna", "give", "up", "on", "you"], "ngguoy", True),
]


class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        return all(s[idx] == val[0] for idx, val in enumerate(words))


for test_case in TEST_CASES:
    assert Solution().isAcronym(test_case[0], test_case[1]) == test_case[2]
