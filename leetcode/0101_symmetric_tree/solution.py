#!/usr/bin/env python

from __future__ import annotations

from typing import Optional

TESTS_INPUT = [([1, 2, 2, 3, 4, 4, 3], True), ([1, 2, 2, None, 3, None, 3], False)]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def print_bin_tree(tree: TreeNode, level: int = 0, prefix: str = "root") -> None:
    print(f"{level * '  '}{prefix:5s}: val={tree.val}")
    if tree.left:
        print_bin_tree(tree.left, level + 1, "left")
    if tree.right:
        print_bin_tree(tree.right, level + 1, "right")


def bin_tree_from_list(tree_list: list[Optional[int]]) -> Optional[TreeNode]:
    if not tree_list:
        return None

    tree = TreeNode(tree_list[0])
    tree_nodes = [tree]

    for idx, val in enumerate(tree_list[1:]):
        if val is None:
            # leaf
            continue

        parent = tree_nodes[idx // 2]
        is_left_node = (idx % 2) == 0
        new_node = TreeNode(val)

        if is_left_node:
            parent.left = new_node
        else:
            parent.right = new_node
        tree_nodes.append(new_node)
    return tree


class Solution:
    def isMirror(self, first: Optional[TreeNode], sec: Optional[TreeNode]) -> bool:
        if not first and not sec:
            return True
        if not first or not sec:
            return False
        return (
            first.val == sec.val
            and self.isMirror(first.left, sec.right)
            and self.isMirror(first.right, sec.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Given the root of a binary tree, check whether it is a mirror
        # of itself (i.e., symmetric around its center).
        if not root:
            return True

        return self.isMirror(root.left, root.right)


for test_case in TESTS_INPUT:
    ans = Solution().isSymmetric(bin_tree_from_list(test_case[0]))
    assert ans == test_case[1]
