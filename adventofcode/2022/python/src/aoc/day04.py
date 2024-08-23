#!/usr/bin/env python

"""Solution for https://adventofcode.com/2022/day/4.

P1: Find how many assignment pairs fully contain the other.

P2: Find how many assignment pairs overlap _at all_.
"""

from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

EXAMPLE_SOLUTION = 2
EXAMPLE_SOLUTION_P2 = 4


def split_line_to_assignments(assignments: str) -> list[list[str]]:
    """Split a list of section cleanups into a nicer pair.

    Args:
        assignments (str): The string representing the section assignments.
            Form is 'w-x,y-z' where w-x is the first elf's sections and
            y-z are the second's sections.

    Returns:
        list[list[str]]: A list of lists, where the first item is a list
            of the first elf's sections, and the second list is the
            list of the second elf's sections.
    """
    return list(map(lambda s: s.split("-"), assignments.split(",")))


def first_inside_second(lhs: list[str], rhs: list[str]) -> bool:
    """Check if the section on the left is entirely within the second.

    Args:
        lhs (list[str]): The section to check if inside the other.
        rhs (list[str]): The section to see if the first fits entirely
            inside.

    Returns:
        bool: True if second section entirely contains the first, false
            otherwise.
    """
    if int(lhs[0]) <= int(rhs[0]) and int(lhs[1]) >= int(rhs[1]):
        return True

    return False


def first_overlaps_second(lhs: list[str], rhs: list[str]) -> bool:
    """Check if the section on the left overlaps _at all_ with the second.

    Args:
        lhs (list[str]): The section to check if has any overlap into the
            second.
        rhs (list[str]): The section to check overlap into against.

    Returns:
        bool: True if any intsersection, false otherwise.
    """
    _lhs = list(map(int, lhs))
    _rhs = list(map(int, rhs))

    if _lhs[0] <= _rhs[0] and _lhs[1] >= _rhs[0]:
        return True

    return False


def check_entirely_overlaps(assignments: str) -> int:
    """Find the total number of entirely overlapping assignments.

    Convert a string of assignments into a numerical value representing
    the total number of assignments that are completely contained within
    their pairing.

    Args:
        assignments (str): The challenge input, representing a list of
            section pairing assignments, one per line.

    Returns:
        int: The toal number of entirely overlapping sections, in either
            direction.
    """
    lhs, rhs = split_line_to_assignments(assignments)

    if first_inside_second(lhs, rhs) or first_inside_second(rhs, lhs):
        return 1

    return 0


def check_any_overlaps(assignments: str) -> int:
    """Find the total number of ANY overlapping assignments.

    Args:
        assignments (str): The challenge input, representing a list of
            section pairing assignments, one per line.

    Returns:
        int: The toal number of ANY overlapping sections, in either
            direction.
    """
    lhs, rhs = split_line_to_assignments(assignments)
    if first_overlaps_second(lhs, rhs) or first_overlaps_second(rhs, lhs):
        return 1

    return 0


def find_part_one(input: str) -> int:
    return sum([check_entirely_overlaps(l) for l in input.split("\n")])


def find_part_two(input: str) -> int:
    return sum([check_any_overlaps(l) for l in input.split("\n")])


def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = load_input(day=4)

    print(f"Part 1: Number of totally overlapped assignments: {find_part_one(inp)}")
    print(f"Part 2: Number of ANY overlapping assignments: {find_part_two(inp)}")


if __name__ == "__main__":
    main()  # pragma: no cover
