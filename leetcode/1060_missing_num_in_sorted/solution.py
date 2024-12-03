#!/usr/bin/env python3

TEST_CASES = [([4, 7, 9, 10], 1, 5), ([4, 7, 9, 10], 3, 8), ([1, 2, 4], 3, 6), ([1], 4, 5)]


class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        missing = []
        start = last = nums[0]

        if len(nums) == 1:
            return start + k

        for num in nums[1:]:
            if num - last > 1:
                # need to add new to missing
                missing += list(range(last + 1, num))
                if len(missing) >= k:
                    return missing[k - 1]

            last = num

        len_missing = len(missing)
        if len_missing >= k:
            return missing[k - 1]

        if not missing:
            return nums[-1] + k
        else:
            return (missing[-1] + 1) + (k - len_missing)


for test_case in TEST_CASES:
    assert Solution().missingElement(test_case[0], test_case[1]) == test_case[2]
