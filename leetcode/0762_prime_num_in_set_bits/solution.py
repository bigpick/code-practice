#!/usr/bin/env python3

# Given two integers, `left` and `right, return ** the count** of numbers in the
# inclusive range `[left, right]` having a prime number of set bits in their binary
# representation
#
# Recall that the number of set bits an integrer has is the number of 1's
#
# For example, `21` when writting in binary is `10101` which as 3 set bits.

TEST_CASES = [(6, 10, 4), (10, 15, 5)]


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def slow_is_prime(num: int) -> bool:
            if num == 0 or num == 1:
                return False

            return all(num % maybe_factor != 0 for maybe_factor in range(2, int(num**0.5) + 1))

        set_bits = 0
        for num in range(left, right + 1):
            num_set_bits = sum([1 for char in bin(num)[2:] if char == "1"])
            print(num_set_bits, num)
            print(slow_is_prime(num_set_bits))

            if slow_is_prime(num_set_bits):
                set_bits += 1

        return set_bits


for test_case in TEST_CASES:
    assert Solution().countPrimeSetBits(test_case[0], test_case[1]) == test_case[2]
