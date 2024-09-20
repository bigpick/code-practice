#!/usr/bin/env python
# ruff: noqa

# > Given an integer k and a string s, find the length of the longest substring that
# > contains at most k distinct characters.
# >
# > For example, given s = "abcba" and k = 2, the longest substring with k
# > distinct characters is "bcb".

TEST_CASES = [
    ("abcba", 2, "bcb"),
    ("eceba", 2, "ece"),
    ("aa", 1, "aa"),
    ("abcdeffg", 3, "effg"),
    ("", 3, ""),
    ("a", 1, "a"),
    ("pipxobsrcgppuguqeksfxrmymngrh", 3, "gppugu"),
    ("pipxobsrcgppuguqeksfxrmymngrh", 4, "cgppugu"),
    ("pipxobsrcgppuguqeksfxrmymngrh", 5, "rcgppugu"),
    ("pipxobsrcgppuguqeksfxnmymngnm", 3, "gppugu"),
    ("pipxobsrcgppuguqeksfxnmymngnm", 4, "nmymngnm"),
    ("pipxobsrcgppuguqeksfxnmymngnm", 5, "xnmymngnm"),
]


def longest_substring_of_distinct_chars(s: str, k: int) -> str:
    if not s:
        return ""

    if len(s) <= k:
        return s

    left = 0
    right = 1
    seen = {}
    seen[s[left]] = 1
    so_far = [s[left]]
    to_return = ""
    while right < len(s):
        next_ = s[right]
        if next_ in seen:
            so_far.append(next_)
            seen[next_] += 1

        elif len(seen) < k:
            # not seen before, but we still have room to get up to k distinct chars
            seen[next_] = 1
            so_far.append(next_)

        else:
            # need to shrink from left until we're back under k, but also have to
            # compare the max(so_far, newest_so_far)?
            to_return = max("".join(so_far), to_return, key=len)
            while len(seen) >= k:
                to_remove = so_far.pop(0)
                seen[to_remove] -= 1
                if seen[to_remove] == 0:
                    del seen[to_remove]

            seen[next_] = 1
            so_far.append(next_)

        right += 1

    return max("".join(so_far), to_return, key=len)


def main():
    for test_case in TEST_CASES:
        ans = longest_substring_of_distinct_chars(test_case[0], test_case[1])
        try:
            assert ans == test_case[2]
        except AssertionError:
            print(f"Test case {test_case[0]} failed.")
            print(f"Wanted: {test_case[2]} || Got: {ans}")
            print("===")


if __name__ == "__main__":
    main()
