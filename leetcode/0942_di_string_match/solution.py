#!/usr/bin/env python3


# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be
# represented as a string s of length n where:
#
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
#
# Given a string s, reconstruct the permutation perm and return it. If there are
# multiple valid permutations perm, return any of them.

TEST_CASES = [("IDID", [0, 4, 1, 3, 2]), ("III", [0, 1, 2, 3]), ("DDI", [3, 2, 0, 1])]


class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        low = 0
        high = len(s)
        to_return = []

        for bwah in s:
            if bwah == "I":
                to_return.append(low)
                low += 1
            else:
                to_return.append(high)
                high -= 1

        to_return.append(low)

        return to_return


for test_case in TEST_CASES:
    assert Solution().diStringMatch(test_case[0]) == test_case[1]
