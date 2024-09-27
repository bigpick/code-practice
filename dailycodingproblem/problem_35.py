#!/usr/bin/env python3

# Problem:
#
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of
# the array so that all the Rs come first, the Gs come second, and the Bs come last. You
# can only swap elements of the array.
#
# Do this in linear time and in-place.
#
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become
# ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

TEST_CASES = [
    (["G", "B", "R"], ["R", "G", "B"]),
    (["R", "B", "G"], ["R", "G", "B"]),
    (["G", "B", "R", "R", "B", "R", "G"], ["R", "R", "R", "G", "G", "B", "B"]),
    (["R"] * 10, ["R"] * 10),
    (["B", "B", "G"], ["G", "B", "B"]),
    (["G", "R", "G"], ["R", "G", "G"]),
    (["B"], ["B"]),
]


def solution(l: list[str]) -> None:
    current = left = 0
    right = len(l) - 1

    while current < len(l):
        if current > right:
            break

        val = l[current]

        # if g, leave it
        if val == "G":
            current += 1
            continue

        # if r, swap to front
        if val == "R":
            # if starts with R
            if current == left:
                current += 1
                left += 1
                continue

            swap_to = l[left]
            l[left] = "R"
            l[current] = swap_to
            left += 1

        # if B, swap to end
        if val == "B":
            swap_to = l[right]
            l[right] = "B"
            l[current] = swap_to
            right -= 1

    return l


for case in TEST_CASES:
    solution(case[0])
    print(case[0])
    assert case[0] == case[1]
