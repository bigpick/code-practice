#!/usr/bin/env python3

# You are given an array `prices` where `prices[i]` is the price of a given stock on
# the `ith` day.
#
# You want to maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.

TEST_CASES = [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0), ([1, 2], 1), ([2, 4, 1], 2)]


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1 or (len(prices) == 2 and prices[0] >= prices[1]):
            return 0

        profit = 0
        minimum = 10e4 + 1

        for price in prices:
            profit = max(profit, price - minimum)
            minimum = min(price, minimum)

        return profit


for test_case in TEST_CASES:
    assert Solution().maxProfit(test_case[0]) == test_case[1]
