#!/usr/bin/env python3

# Given a positive integer n, write a function that returns the number of
# set bits in its binary representation (also known as the Hamming weight).

from time import perf_counter

TEST_CASES = [
    (11, 3),
    (128, 1),
    (2147483645, 30)
]

class Solution:
    def hammingWeight(self, n: int) -> int:
        # bin(n) -> 0b 1011
        return sum([1 for x in bin(n)[2:] if x == "1"])

    def hammingWeightBitwise(self, n: int) -> int:
        one_bits = 0
        while n:
            if n&1:
                one_bits += 1
            n = n >> 1
        return one_bits

for test_case in TEST_CASES:
    assert Solution().hammingWeight(test_case[0]) == test_case[1]
    assert Solution().hammingWeightBitwise(test_case[0]) == test_case[1]

times = []
for expo in range(500):
    chal = 10**expo
    start = perf_counter()
    Solution().hammingWeightBitwise(chal)
    times.append(perf_counter() - start)

for t in times:
    print(t)
