#!/usr/bin/env python3

# You are given a license key represented as a string s that consists of only alphanumeric
# characters and dashes. The string is separated into n + 1 groups by n dashes. You
# are also given an integer k.
#
# We want to reformat the string s such that each group contains exactly k characters,
# except for the first group, which could be shorter than k but still must contain at
# least one character. Furthermore, there must be a dash inserted between two groups,
# and you should convert all lowercase letters to uppercase.
#
# Return the reformatted license key.

TEST_CASES = [("5F3Z-2e-9-w", 4, "5F3Z-2E9W"), ("2-5g-3-J", 2, "2-5G-3J")]


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        so_far = 0
        to_return = ""
        for val in s[::-1]:
            if val == "-":
                continue

            if so_far < k:
                to_return += val.upper()
                so_far += 1
            else:
                to_return += "-"
                to_return += val.upper()
                so_far = 1

        return to_return[::-1]


for test_case in TEST_CASES:
    assert Solution().licenseKeyFormatting(test_case[0], test_case[1]) == test_case[2]
