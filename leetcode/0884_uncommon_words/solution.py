#!/usr/bin/env python3

TEST_CASES = [
    ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
    ("apple apple", "banana", ["banana"]),
]


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        seen = {}
        for word in s1.split() + s2.split():
            try:
                seen[word] += 1
            except KeyError:
                seen[word] = 1

        to_return = []
        for key, val in seen.items():
            if val == 1:
                to_return.append(key)

        return to_return


for test_case in TEST_CASES:
    assert Solution().uncommonFromSentences(test_case[0], test_case[1]) == test_case[2]
