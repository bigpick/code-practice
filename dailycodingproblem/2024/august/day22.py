#!/usr/bin/env python

# Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k.

from typing import Optional


TEST_PAIRS = [
    ([10, 15, 3, 7], 17, True),
    ([10, 15, 3, 7], 19, False),
    ([10, 15, 3, 7], 25, True),
    ([10, 15, 3, 7], 10, True),
    ([10, 15, 3, 7], 15, False),
]

TEST_PAIRS_IDX = [
    ([10, 15, 3, 7], 17, (0, 3)),
    ([10, 15, 3, 7], 19, (None, None)),
    ([10, 15, 3, 7], 25, (0, 1)),
    ([10, 15, 3, 7], 10, (2, 3)),
    ([10, 15, 3, 7], 15, (None, None)),
]


def any_two(input_list: list[int], k: int) -> bool:
    seen = {}
    for idx, item in enumerate(input_list):
        complement = k - item
        if seen.get(complement, None) is not None:
            return True

        seen[item] = idx

    return False


def any_two_idxs(input_list: list[int], k: int) -> tuple[Optional[int], Optional[int]]:
    seen = {}
    for idx, item in enumerate(input_list):
        complement = k - item
        if (complement_idx := seen.get(complement, None)) is not None:
            return complement_idx, idx

        seen[item] = idx

    return None, None


for test_case in TEST_PAIRS:
    assert any_two(test_case[0], test_case[1]) == test_case[2]

for test_case in TEST_PAIRS_IDX:
    assert any_two_idxs(test_case[0], test_case[1]) == test_case[2]
