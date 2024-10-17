#!/usr/bin/env python3

TEST_CASES = [("USA", True), ("FlaG", False), ("leetcode", True), ("lfAG", False)]


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        from string import ascii_uppercase

        cap = 0
        for c in word:
            if c in ascii_uppercase:
                cap += 1

        return cap == 0 or cap == len(word) or (cap == 1 and word[0] in ascii_uppercase) or False


for test_case in TEST_CASES:
    assert Solution().detectCapitalUse(test_case[0]) == test_case[1]
