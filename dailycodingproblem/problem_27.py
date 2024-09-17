#!/usr/bin/env python3

# > Good morning! Here's your coding interview problem for today.
# >
# > This problem was asked by Facebook.
# >
# > Given a string of round, curly, and square open and closing brackets, return
# > whether the brackets are balanced (well-formed).
# >
# > For example, given the string "([])[]({})", you should return true.
# >
# > Given the string "([)]" or "((()", you should return false.

from collections import deque

TESTS = [
    ("([])[]({})", True),
    ("([)]\\", False),
    ("((()\\", False),
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("(((", False),
    ("([])", True),
]


def is_valid(thingy: bool) -> bool:
    # Also the same as Leetcode problem # 20. Valid Parentheses
    left = {"(": ")", "[": "]", "{": "}"}

    d = deque()
    for thing in thingy:
        if thing in left:
            d.append(thing)
        else:
            try:
                last = d.pop()
            except IndexError:
                # deque is empty, but we saw a right-handed thing
                # - eg, "]"
                return False

            if left[last] != thing:
                return False

    return len(d) == 0


for case in TESTS:
    assert is_valid(case[0]) == case[1]
