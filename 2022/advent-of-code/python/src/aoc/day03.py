#!/usr/bin/env python

"""Solution for https://adventofcode.com/2022/day/3.

P1:
in the given input (elves distinguished by empty newlines)

P2:
"""

from collections.abc import Iterable
from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

EXAMPLE_SOLUTION = 157
EXAMPLE_SOLUTION_P2 = 70


def get_common_item_priority_score(c: str) -> int:
    """Find the priority score of a given rucksack item.

    a-z are worth 1-26, while A-Z are worth 27-52.

    Args:
        c (str): The rucksack item to find the value of.

    Returns:
        int: The value of the rucksack item, as defined by the challenge.
    """
    if c.islower():
        return ord(c) - 96

    # Account for the difference between a->Z (-32), as well as the fact
    # that we're starting at 27 and not 1 (+26)
    return (ord(c) - (96 - 32)) + 26


def line_to_rucksack(inv_line: str) -> str:
    """Find the common inventory item contained within a rucksack's two inventory compartments.

    The rucksack is guranteed to be evenly divisible in two equal halves,
    and there will always be at least and at most 1 common item between
    the two.

    Args:
        inv_line (str): The rucksack to find the matching

    Returns:
        str: The common item between the rucksack's two compartments.
    """
    midway = len(inv_line) // 2
    return set(inv_line[0:midway]).intersection(set(inv_line[midway:])).pop()


def find_priority_sum_each_rucksack(input: list[str]) -> int:
    """Calculate the solution for part one.

    Args:
        input (list[str]): The given input, each line representing a rucksack.

    Returns:
        int: The sum of all shared item's priority value for every rucksack.
    """
    return sum([get_common_item_priority_score(line_to_rucksack(line)) for line in input])


def take_chunks(l: list[str], size: int) -> Iterable[list[str]]:
    """Split a given list into N many chunks of size _size_.

    Args:
        l (list[str]): The list to split.
        size (int): The size of sublists to chunk into.

    Returns:
        Iterable[list[str]]: A chunk of the original list of size _size.
    """
    for i in range(0, len(l), size):
        yield l[i : i + size]


def get_common_from_three_rucksacks(rucksacks: list[str]) -> str:
    """Find the common item between three rucksacks.

    It's guranteed there will always be at least and at most one common
    item across all three.

    Args:
        rucksacks (list[str]): The list of rucksacks to find the common
            item from.

    Returns:
        str: The shared inventory item of all three rucksacks.
    """
    return set.intersection(*list(map(set, rucksacks))).pop()  # type: ignore


def find_priority_of_3sum(input: list[str]) -> int:
    """Calculate the solution for part two.

    Args:
        input (list[str]): The given input, each line representing a rucksack.

    Returns:
        int: The sum of all 3-rucksack pairings' shared item's priority value.
    """
    return sum(
        [
            get_common_item_priority_score(get_common_from_three_rucksacks(elf_3some))
            for elf_3some in take_chunks(input, 3)
        ]
    )


def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = load_input(day=3).strip().split()

    p1 = find_priority_sum_each_rucksack(inp)
    p2 = find_priority_of_3sum(inp)
    print(f"Part 1: Sum of priority of common item in each rucksack: {p1}")
    print(f"Part 2: Sum of threesome rucksack pairings: {p2}")


if __name__ == "__main__":
    main()  # pragma: no cover
