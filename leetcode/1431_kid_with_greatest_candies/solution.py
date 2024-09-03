#!/usr/bin/env python3

# There are n kids with candies. You are given an integer array candies, where
# each candies[i] represents the number of candies the ith kid has, and an integer
# extraCandies, denoting the number of extra candies that you have.
#
# Return a boolean array result of length n, where result[i] is true if, after
# giving the ith kid all the extraCandies, they will have the greatest number of
# candies among all the kids, or false otherwise.
#
# Note that multiple kids can have the greatest number of candies.

TEST_CASES = [
    ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
    ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
    ([12, 1, 12], 10, [True, False, True]),
]


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        most_candy = max(candies)
        results = [False] * len(candies)
        for idx, kid in enumerate(candies):
            if kid + extraCandies >= most_candy:
                results[idx] = True

        return results


for test_case in TEST_CASES:
    print(Solution().kidsWithCandies(test_case[0], test_case[1]))
    assert Solution().kidsWithCandies(test_case[0], test_case[1]) == test_case[2]
