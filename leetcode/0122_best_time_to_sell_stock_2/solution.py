#!/usr/bin/env python3

# You are given an array `prices` where `prices[i]` is the price of a given stock on
# the `ith` day.
#
# On each day, you may decide to buy and/or sell the stock. You can only hold at most
# one share of the stock at any time. However, you can buy it then immediately sell
# it on the same day.
#
# Find and return the maximum profit you can achieve.

# This is different than the "simpler" case because now you can buy/sell as many times
# as you want, to try to maximize profit. so its more of a moving local minimum thing

TEST_CASES = [([7, 1, 5, 3, 6, 4], 7), ([1, 2, 3, 4, 5], 4), ([7, 6, 4, 3, 1], 0)]


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2 or (len(prices) == 2 and prices[1] < prices[0]):
            return 0

        profit = 0
        for idx, price in enumerate(prices[:-1]):
            price_diff = prices[idx + 1] - price
            if price_diff > 0:
                profit += price_diff
        return profit


for test_case in TEST_CASES:
    assert Solution().maxProfit(test_case[0]) == test_case[1]
