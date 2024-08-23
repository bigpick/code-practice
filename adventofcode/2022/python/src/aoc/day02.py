#!/usr/bin/env python

"""Solution for https://adventofcode.com/2022/day/2.

P1: Rock paper scissors tournament.

    A/X -> Rock, B/Y -> Paper, C/Z -> Scissors.

First column is opponent play, second column is ???. Scores are based
on shape; Rock 1, paper 2, scissors 3 and whether or not you won (0
for loss, 3 for draw, 6 if won). Calculate the score if you were to
follow the given strategy guide.

P2: It turns out that the second column is actually how the round needs
to end.

    X -> lose, Y -> draw, Z -> win

Scoring is calculated the same. Now calculate the end score if you were
to play as the second column dictates your results.
"""

from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """A Y
B X
C Z
"""
EXAMPLE_SOLUTION = 15
EXAMPLE_SOLUTION_P2 = 12

rps_outcomes = {
    "AX": "tie",
    "AY": "win",
    "AZ": "loss",
    "BX": "loss",
    "BY": "tie",
    "BZ": "win",
    "CX": "win",
    "CY": "loss",
    "CZ": "tie",
}

rps_values = {"win": 6, "loss": 0, "tie": 3, "X": 1, "Y": 2, "Z": 3}

expected_outcomes = {"X": "loss", "Y": "tie", "Z": "win"}
outcomes = {
    "X": {"A": "Y", "B": "Z", "C": "X"},  # lose
    "Y": {"A": "X", "B": "Y", "C": "Z"},  # tie
    "Z": {"A": "Z", "B": "X", "C": "Y"},  # win
}


class RockPaperScissorsGame:
    def __init__(self, matchup: str) -> None:
        self.p1, self.p2 = matchup.split()
        self.match = self.p1 + self.p2

    def get_round_score(self) -> int:
        return rps_values[rps_outcomes[self.match]] + rps_values[self.p2]

    def __str__(self) -> str:
        return f"{self.p1} vs {self.p2}"  # pragma: no cover

    @staticmethod
    def from_str(input: str):
        return sum([RockPaperScissorsGame(match).get_round_score() for match in input.split("\n")])


class FixedRPSGame:
    def __init__(self, matchup: str) -> None:
        self.p1, self.expected_outcome = matchup.split()

    def get_round_score(self) -> int:
        needed_matchup = [
            k
            for k in rps_outcomes.keys()
            if k[0] == self.p1 and rps_outcomes[k] == expected_outcomes[self.expected_outcome]
        ][0]

        return rps_values[needed_matchup[1]] + rps_values[expected_outcomes[self.expected_outcome]]

    @staticmethod
    def from_str(input: str):
        return sum([FixedRPSGame(match).get_round_score() for match in input.split("\n")])


def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = load_input(day=2)

    p1 = RockPaperScissorsGame.from_str(inp)
    p2 = FixedRPSGame.from_str(inp)

    print(f"Part 1: Total score: {p1}")
    print(f"Part 2: Total score: {p2}")


if __name__ == "__main__":
    main()  # pragma: no cover
