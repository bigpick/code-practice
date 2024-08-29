#!/usr/bin/env python3

from __future__ import annotations

from typing import Optional


def print_node(node: Optional[Node], level: int = 0) -> None:
    if node is not None:
        print_node(node.right, level + 1)
        print(" " * 4 * level + "-> " + str(node.value))
        print_node(node.left, level + 1)


class Node:
    def __init__(
        self, value: Optional[int] = None, left: Optional[Node] = None, right: Optional[Node] = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        print_node(self)
        return ""


t = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(t)


def count_unival_trees(node: Node) -> int:
    class Counter:
        val = 0

    def is_unival_tree(node: Node) -> bool:
        if node is None:
            return True

        left_unival = is_unival_tree(node.left)
        right_unival = is_unival_tree(node.right)

        if not left_unival or not right_unival:
            return False

        l_val = node.left.value if node.left is not None else node.value
        r_val = node.right.value if node.right is not None else node.value

        if l_val == r_val == node.value:
            Counter.val += 1
            return True

        return False

    is_unival_tree(t)
    return Counter.val


print(t)
assert count_unival_trees(t) == 5
t2 = Node(1, Node(1, Node(1)), Node(1, Node(1), Node(1)))

print(t2)
assert count_unival_trees(t2) == 5
