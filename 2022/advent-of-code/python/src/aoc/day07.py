#!/usr/bin/env python

"""Solution for https://adventofcode.com/2022/day/7.

P1: Find all of the directories with a total size of at most 100000,
then calc the sum of their total sizes.

P2:
"""

from os.path import split, join
from aoc.common import load_input, show_current_day

EXAMPLE_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
EXAMPLE_SOLUTION = None
EXAMPLE_SOLUTION_P2 = None

TOTAL_FS_SIZE = 70000000
REQUIRED_SIZE = 30000000


def split_input_to_commands(input: str) -> list[str]:
    return list(map(lambda s: s.removeprefix("$").lstrip(), input.split("\n$")))


def convert_path_to_parents(p: str) -> list[str]:
    full_paths: list[str] = []
    parent, curdir = split(p)
    full_paths.append(join(parent, curdir))
    while parent and curdir:
        parent, curdir = split(parent)
        full_paths.append(join(parent, curdir))

    return full_paths


class Filesystem:
    def __init__(self) -> None:
        self.tree = {"/": 0}
        self.cur_dir = ""

    def eat_command(self, command: str):
        command, *results = command.split("\n")
        if command[:2] == "cd":
            dir = command.split()[-1]
            if dir == "..":
                self.cur_dir = "/".join(self.cur_dir.split("/")[:-1])
            elif dir == "/":
                self.cur_dir = "/"
            else:
                self.cur_dir = self.cur_dir.rstrip("/") + f"/{dir}"
        else:
            # ls
            for entry in results:
                if entry[0] == "d":
                    continue

                fsize = int(entry.split()[0])
                for p in convert_path_to_parents(self.cur_dir):
                    try:
                        self.tree[p] += fsize
                    except KeyError:
                        self.tree[p] = fsize

    def get_size_paths_less_than(self, size: int) -> int:
        return sum([v for v in self.tree.values() if v <= size])

    def get_total_usage(self) -> int:
        return TOTAL_FS_SIZE - self.tree["/"]

    def get_min_free_required(self) -> int:
        return REQUIRED_SIZE - self.get_total_usage()

    def find_smallest_possible_to_free(self) -> int:
        to_free = self.get_min_free_required()
        for v in sorted(self.tree.values()):
            if v >= to_free:
                return v
        return -1

    def __str__(self) -> str:
        return str(self.tree)


def find_part_one(input: str):
    fs = Filesystem()

    for c in split_input_to_commands(input):
        fs.eat_command(c)

    return fs.get_size_paths_less_than(100000)


def find_part_two(input: str):
    fs = Filesystem()

    for c in split_input_to_commands(input):
        fs.eat_command(c)

    return fs.find_smallest_possible_to_free()


def main():  # pragma: no cover
    print(show_current_day(__file__))
    inp = load_input(day=7)

    # print(convert_path_to_parents("/a/b/c"))
    # fs = Filesystem()
    # for c in split_input_to_commands(EXAMPLE_INPUT):
    #     fs.eat_command(c)
    # print(fs)
    # print(fs.get_size_paths_less_than(100000))
    # print(fs.find_smallest_possible_to_free())
    print(f"Part 1: {find_part_one(inp)}")
    print(f"Part 2: {find_part_two(inp)}")


if __name__ == "__main__":
    main()  # pragma: no cover
