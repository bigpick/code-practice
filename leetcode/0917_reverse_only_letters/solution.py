#!/usr/bin/env python3

# Given a string s, reverse the string according to the following rules:
#
#     All the characters that are not English letters remain in the same position.
#     All the English letters (lowercase or uppercase) should be reversed.
#
# Return s after reversing it.


TEST_CASES = [
    ("ab-cd", "dc-ba"),
    ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
    ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
    ("7_28]", "7_28]"),
]


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        from string import ascii_letters as alpha

        left = 0
        right = len(s) - 1

        list_s = list(s)

        if len(s) == 1:
            return s

        while left < right:
            while list_s[left] not in alpha:
                left += 1
                if left > right:
                    return "".join(list_s)

            while list_s[right] not in alpha:
                right -= 1
                if right < left:
                    return "".join(list_s)

            temp = list_s[right]
            list_s[right] = list_s[left]
            list_s[left] = temp
            right -= 1
            left += 1

        return "".join(list_s)

        pass


for test_case in TEST_CASES:
    assert Solution().reverseOnlyLetters(test_case[0]) == test_case[1]
