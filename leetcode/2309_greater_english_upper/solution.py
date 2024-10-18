#!/usr/bin/env python3

# Given a string of English letters s, return the greatest English letter which occurs
# as both a lowercase and uppercase letter in s. The returned letter should be in
# uppercase. If no such letter exists, return an empty string.
#
# An English letter b is greater than another letter a if b appears after a in the
# English alphabet.

TEST_CASES = [("lEeTcOdE", "E"), ("arRAzFif", "R"), ("AbCdEfGhIjK", ""), ("Aa", "A")]


class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = {}
        lower_a = ord("a")
        lower_z = ord("z")

        greatest = -1

        for char in s:
            c_code = ord(char)
            c_code_tracker = c_code
            modifier = 32
            if c_code >= lower_a and c_code <= lower_z:
                # is lowercase
                modifier = -32
                c_code_tracker += modifier

            try:
                seen[c_code + modifier]
                greatest = max(greatest, c_code_tracker)
            except KeyError:
                pass

            seen[c_code] = 1

        return chr(greatest) if greatest > 0 else ""


for test_case in TEST_CASES:
    print(Solution().greatestLetter(test_case[0]))
    # assert Solution().greatestLetter(test_case[0]) == test_case[1]
