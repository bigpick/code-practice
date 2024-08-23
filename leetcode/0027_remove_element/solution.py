#!/usr/bin/env python

TESTS_INPUT = [
        ([3, 2, 2, 3], 3, 2, [2, 2, 0, 0]),
        ([0,1,2,2,3,0,4,2], 2, 5, [0,1,3,0,4]),

        ]


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Given an integer array nums and an integer val, remove all occurrences of
        # val in nums in-place. The order of the elements may be changed. Then return
        # the number of elements in nums which are not equal to val.
        #
        # Consider the number of elements in nums which are not equal to val be k, to
        # get accepted, you need to do the following things:
        #
        # Change the array nums such that the first k elements of nums contain
        # the elements which are not equal to val. The remaining elements of nums are
        # not important as well as the size of nums.
        sofar = 0
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == val:
                nums.pop(idx)
            else:
                sofar += 1

        return sofar


for test_case in TESTS_INPUT:
    ans = Solution().removeElement(test_case[0], test_case[1])
    assert ans == test_case[2]
    print(test_case[0])
    assert test_case[0][: test_case[2]] == test_case[3][: test_case[2]]
