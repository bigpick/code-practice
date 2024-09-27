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


def testerrrr(size: int) -> None:
    from copy import deepcopy
    from random import shuffle

    ans = (["R"] * (size//3)) + (["G"] *(size//3))+ (["B"] * (size//3))
    chall = deepcopy(ans)

    for _ in range(10):
        shuffle(chall)

    return chall, ans


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


from time import perf_counter
for size in (100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000):
    chall, ans = testerrrr(size)
    start = perf_counter()
    solution(chall)
    print(f"{size} took {perf_counter() - start }")
    assert chall == ans

#for case in TEST_CASES:
#    #for size in (100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000):
#    for size in (100, 1_000, 10_000, 100_000): # 1_000_000, 10_000_000):
#        chall, ans = testerrrr(size)
#        start = perf_counter()
#        solution(chall)
#        print(f"{size} took {perf_counter() - start }")
#        assert chall == ans
#
#    #solution(case[0])
#    #print(case[0])
#    #assert case[0] == case[1]
