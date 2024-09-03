#!/usr/bin/env python3

# You are given two strings word1 and word2. Merge the strings by adding letters in
# alternating order, starting with word1. If a string is longer than the other, append
# the additional letters onto the end of the merged string.
#
# Return the merged string.

TEST_CASES = [("abc", "pqr", "apbqcr"), ("ab", "pqrs", "apbqrs"), ("abcd", "pq", "apbqcd")]


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_size = len(word1)
        word2_size = len(word2)

        min_size = min(word1_size, word2_size)
        max_size = max(word1_size, word2_size)

        new = ""
        for i in range(min_size):
            new += word1[i] + word2[i]

        if min_size == max_size:
            return new

        if word1_size > word2_size:
            return new + word1[i + 1 :]

        return new + word2[i + 1 :]


for test_case in TEST_CASES:
    print(Solution().mergeAlternately(test_case[0], test_case[1]))
    assert Solution().mergeAlternately(test_case[0], test_case[1]) == test_case[2]
