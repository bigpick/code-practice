#!/usr/bin/env python

"""Solution for https://adventofcode.com/2022/day/1.

P1: Goal is to find the elf with the most calories; return index of elf
in the given input (elves distinguished by empty newlines)

P2: Want to know the top THREE elves.
"""

from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def get_elfs_cumulative_cals(cals: str) -> int:
    """Find the total sum worth of calories an elf is worth.

    Input is expected to be a newline separated list of strings
    representing the number of calories per-snack and elf has in it's
    inventory.

    Args:
        cals (str): The list of calories per snack an elf has in it's
            inventory. Expected to be a newline seprated list of strings
            representing the integer value of each snack's total calorie
            worth.

    Returns:
        int: The sum of all the elf's snacks calories.
    """
    return sum(map(int, cals.split()))


def rank_elves(elf_inv: str, top_n: int = 1) -> int:
    """Find the top N elves worth of snack calories among a list of elves and return its sum.

    Args:
        elf_inv (str): The list of elves and their inventory indicating
            each elf's snack inventory, and each snack's caloric value.
            Elves are represented as a contiguous set of newline separated
            strings representing the integer value of a snack's calories.
        top_n (int): The number of N-many top elves' calories you intend
            to find the sum of.

    Returns:
        int: The total number of calories contained within the top top_n
            many elves' caloric counts.
    """
    elf_inv = elf_inv.split("\n\n")  # type: ignore
    calorie_sums_for_each_elf = list(map(get_elfs_cumulative_cals, elf_inv))
    top_calorie_elves = sorted(calorie_sums_for_each_elf, reverse=True)[:top_n]
    return sum(top_calorie_elves)


def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = load_input(day=1)

    print(f"Part 1: The elf with the most calories totals {rank_elves(inp)}.")
    print(f"Part 2: The top three elves with most calories totals {rank_elves(inp, 3)}.")


if __name__ == "__main__":
    main()  # pragma: no cover
