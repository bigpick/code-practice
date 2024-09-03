#!/usr/bin/env python

# You are given a 0-indexed array of integers nums of length n. You are initially
# positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
#
#    0 <= j <= nums[i] and
#    i + j < n
#
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].

TESTS_INPUT = [
    ([2, 3, 1, 1, 4], 2),
    ([2, 3, 0, 1, 4], 2),
    ([1, 3, 2], 2),
    ([1, 2, 3, 4, 5], 3),
    ([1, 1, 1, 1], 3),
    ([1, 2, 1, 1, 1], 3),
    ([2, 1, 1, 1, 1], 3),
]


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if not nums or len(nums) == 1:
            return 0

        idx = 0
        hops = 0
        size = len(nums) - 1
        while True:
            max_ = -1
            gas = nums[idx]
            # print(idx, gas)
            # print(f"{idx=}")
            for i in range(idx + 1, idx + gas + 1):
                # print(f"{i=}")
                if i == size:
                    # print("returning i = size")
                    return hops + 1

                if (val := nums[i]) > max_:
                    max_ = val
                    next_idx = i

            hops += 1
            idx = next_idx
            # print(f"{idx=} || {hops=}")
            if gas + idx >= size:
                return hops

        return hops


for test_case in TESTS_INPUT:
    print(test_case[0])
    print(Solution().canJump(test_case[0]))
    assert Solution().canJump(test_case[0]) == test_case[1]
