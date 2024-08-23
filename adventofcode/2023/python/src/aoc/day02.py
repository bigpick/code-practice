#!/usr/bin/env python

"""Solution for https://adventofcode.com/2023/day/2.

P1: What is the sum of the IDs of those games w/ with only 12 red cubes,
13 green cubes, and 14 blue cubes (with replacement)?

P2:
"""

from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
EXAMPLE_SOLUTION = 8
EXAMPLE_SOLUTION_P2 = 2286


def is_valid_round(pull: dict[bytes, bytes], max_red: int, max_green: int, max_blue: int):
    return (
        int(pull.get("red", 0)) <= max_red
        and int(pull.get("green", 0)) <= max_green
        and int(pull.get("blue", 0)) <= max_blue
    )


def find_id_sums(
    games: list[str], max_red: int = 12, max_green: int = 13, max_blue: int = 14
) -> int:
    total: int = 0
    for game in games:
        valid_round = True
        game_id, game = game.split(":")
        game_id = int(game_id.split()[-1])

        for round in game.split(";"):
            scores = dict([tuple(pull.strip().split()[::-1]) for pull in round.split(",")])  # type: ignore
            if not is_valid_round(scores, max_red, max_green, max_blue):
                valid_round = False

        if valid_round:
            total += game_id

    return total


def maybe_raise_max(mins: dict[str, int], scores: dict[str, int]) -> None:
    for c in ["red", "green", "blue"]:
        try:
            score = int(scores[c])
        except KeyError:
            score = 0

        if score > mins[c]:
            mins[c] = score


def get_power(mins: dict[str, int]) -> int:
    return mins["green"] * mins["blue"] * mins["red"]


def find_power_sums(games: list[str]) -> int:
    sum_ = 0
    for game in games:
        mins = {"red": 0, "green": 0, "blue": 0}
        for round in game.split(":")[1].split(";"):
            scores = dict([tuple(pull.strip().split()[::-1]) for pull in round.split(",")])  # type: ignore
            maybe_raise_max(mins, scores)  # type: ignore
        sum_ += get_power(mins)
    return sum_


def find_part_one(input: list[str]):
    return find_id_sums(input)


def find_part_two(input: list[str]):
    return find_power_sums(input)


def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = [line.strip() for line in load_input(day=2).split("\n")]

    print(f"Part 1: {find_part_one(inp)}")
    print(f"Part 2: {find_part_two(inp)}")


if __name__ == "__main__":
    main()  # pragma: no cover
